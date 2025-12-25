# src/004_app.py
# Advanced, multi-page Dash dashboard for Customer Segmentation

import dash
from dash import dcc, html, dash_table
from dash_extensions.enrich import Output, Input, dcc, State
import pandas as pd 
import joblib
from pathlib import Path
import plotly.express as px
import base64
import io
from io import StringIO

from dash import ctx
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import tempfile

# --- Load Artifacts ---
try:
    artifacts = {
        "kmeans_model": joblib.load("artifacts/kmeans_model.pkl"),
        "scaler": joblib.load("artifacts/scaler.pkl"),
        "supervised_model": joblib.load("artifacts/supervised_model.pkl"),
        "supervised_scaler": joblib.load("artifacts/supervised_scaler.pkl"),
        "label_encoder": joblib.load("artifacts/label_encoder.pkl"),
    }
    artifacts_loaded = True
except FileNotFoundError:
    artifacts_loaded = False

# --- Initialize the Dash App ---
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

# --- Helper Functions ---

#start of predict section 
def predict_segments(df):
    df_copy = df.copy()

    # Normalize column names (remove spaces, lower case for detection)
    df_copy.columns = [col.strip() for col in df_copy.columns]
    cols_lower = [c.lower() for c in df_copy.columns]

    # --- Auto-detect transactional data (more flexible) ---
    has_raw_data = (
        any('invoice' in c for c in cols_lower) and
        any('date' in c for c in cols_lower) and
        any('customer' in c for c in cols_lower) and
        any('quantity' in c for c in cols_lower) and
        any(('price' in c or 'amount' in c or 'sales' in c) for c in cols_lower)
    )

    if has_raw_data:
        # Map column names dynamically
        invoice_col = next(c for c in df_copy.columns if 'invoice' in c.lower())
        date_col = next(c for c in df_copy.columns if 'date' in c.lower())
        cust_col = next(c for c in df_copy.columns if 'customer' in c.lower())
        qty_col = next(c for c in df_copy.columns if 'quantity' in c.lower())
        price_col = next(c for c in df_copy.columns if any(x in c.lower() for x in ['price', 'amount', 'sales']))

        # Clean and compute totals
        df_copy.dropna(subset=[cust_col], inplace=True)
        df_copy = df_copy[df_copy[qty_col] > 0]
        df_copy['TotalPrice'] = df_copy[qty_col] * df_copy[price_col]

        # Parse dates safely
        df_copy[date_col] = pd.to_datetime(df_copy[date_col], errors='coerce')

        # --- Compute RFM metrics ---
        latest_date = df_copy[date_col].max()
        rfm = df_copy.groupby(cust_col).agg({
            date_col: lambda x: (latest_date - x.max()).days,
            invoice_col: 'nunique',
            'TotalPrice': 'sum'
        }).reset_index()

        rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
        df_copy = rfm

    else:
        # Expect that Recency, Frequency, Monetary already exist
        required = ['Recency', 'Frequency', 'Monetary']
        if not all(col in df_copy.columns for col in required):
            raise ValueError(
                "Uploaded file must contain either raw transactional columns "
                "(InvoiceNo, InvoiceDate, CustomerID, Quantity, UnitPrice / Amount / Sales) "
                "or precomputed RFM columns (Recency, Frequency, Monetary)."
            )

    # --- Drop missing or invalid values before prediction ---
    df_copy = df_copy.dropna(subset=["Recency", "Frequency", "Monetary"])
    df_copy = df_copy[(df_copy["Recency"] >= 0) & (df_copy["Frequency"] > 0) & (df_copy["Monetary"] > 0)]

    # --- Predict segments ---
    X_scaled = artifacts["scaler"].transform(df_copy[["Recency", "Frequency", "Monetary"]])
    df_copy["Cluster"] = artifacts["kmeans_model"].predict(X_scaled)

    X_scaled_sup = artifacts["supervised_scaler"].transform(df_copy[["Recency", "Frequency", "Monetary"]])
    seg_pred = artifacts["supervised_model"].predict(X_scaled_sup)
    df_copy["Segment"] = artifacts["label_encoder"].inverse_transform(seg_pred)

    return df_copy



#end of predict section 

# --- App Layout ---
sidebar = html.Div([
    html.Button("«", id="hide-sidebar-btn"), # NEW: Hide button
    html.H2("Dashboard Navigation"), html.Hr(),
    html.P("Select a page to view"),
    html.Div([
        dcc.Link("Project Overview", href="/"),
        dcc.Link("Explore Segments", href="/explore-segments"),
        dcc.Link("Single Prediction", href="/single-prediction"),
        dcc.Link("Model Performance", href="/model-performance"),
        dcc.Link("Cohort Analysis", href="/cohort-analysis"),

    ], id="nav-links")
], id="sidebar")

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Button("»", id="show-sidebar-btn", style={'display': 'none'}), # NEW: Show button
    sidebar,
    html.Div(id="page-content")
], id="app-container")

# --- Page Layouts (as functions) ---
def build_overview_layout():
    return html.Div([
        html.Div([
            html.Div([
                html.H1("Unlock Customer Insights"),
                dcc.Markdown("Transform raw sales data into actionable business strategy with advanced RFM segmentation."),
            ]),
            html.Img(src=app.get_asset_url('hero-image.png'), style={'max-width': '350px'}) # Add a hero image to your assets folder
        ], className="overview-header"),
        html.Div([
            html.Div([html.P("Total Customers Analyzed"), html.H2("4,338", className="stat-number")], className="stat-card"),
            html.Div([html.P("Identified Segments"), html.H2("4", className="stat-number")], className="stat-card"),
            html.Div([html.P("Model Accuracy"), html.H2("99.8%", className="stat-number")], className="stat-card"),
        ], style={'display': 'grid', 'gridTemplateColumns': '1fr 1fr 1fr', 'gap': '20px'}),
    ])

def build_explore_layout():
    return html.Div([
        html.H1("🔎 Explore & Analyze Segments"),
        html.P("Upload your customer data to segment them and drill down into individual profiles."),
        dcc.Upload(
            id='upload-data',
            children=html.Div([
                html.Div([
                    html.Span("☁️", className="icon"),
                    html.Span("Drag, Drop, or Click to Upload"),
                ], className="uploader-text-icon"),
                html.Button('Browse Files', className='button'),
            ], className='custom-uploader-container'),
            style={'width': '100%', 'height': 'auto', 'lineHeight': '60px', 'borderWidth': '0', 'borderRadius': '15px'},
            multiple=False
        ),
        html.Hr(),
        dcc.Store(id='stored-results-data', storage_type='session'),
        dcc.Download(id="download-pdf"),

        html.Div(id='explore-output-container'),
        html.Div(id='customer-drilldown-section', style={'display': 'none'})
    ])
#adding live atbles for single prection 

def build_predict_layout():
    return html.Div([
        html.H1("🔮 Single Customer Prediction"),
        html.P("Adjust the sliders to explore how Recency, Frequency, and Monetary values affect the predicted customer segment."),

        # --- RFM Input Sliders ---
        html.Div([
            html.Div([
                html.Label("Recency (days)"),
                dcc.Slider(id='recency-slider', min=0, max=200, step=1, value=50,
                           marks={0:'0', 50:'50', 100:'100', 150:'150', 200:'200'})
            ], style={'width': '30%', 'padding': '10px'}),

            html.Div([
                html.Label("Frequency (orders)"),
                dcc.Slider(id='frequency-slider', min=1, max=50, step=1, value=5,
                           marks={1:'1', 10:'10', 20:'20', 30:'30', 50:'50'})
            ], style={'width': '30%', 'padding': '10px'}),

            html.Div([
                html.Label("Monetary (spend)"),
                dcc.Slider(id='monetary-slider', min=100, max=10000, step=100, value=1000,
                           marks={100:'100', 2000:'2k', 5000:'5k', 8000:'8k', 10000:'10k'})
            ], style={'width': '30%', 'padding': '10px'})
        ], style={'display': 'flex', 'justifyContent': 'space-around'}),

        html.Hr(),

        html.Div(id='prediction-output', style={'fontSize': 26, 'fontWeight': 'bold', 'textAlign': 'center', 'marginTop': '20px'}),

        html.Div([
            dcc.Graph(id='rfm-profile-chart')
        ], style={'marginTop': '30px'})
    ])


#ending #adding live atbles for single prection 

def build_performance_layout():
    return html.Div([
        html.H1("📈 Model Performance Evaluation"),
        html.Div([
            html.Div("Unsupervised Model (K-Means)", id="tab-unsupervised", n_clicks=0, className="tab selected"),
            html.Div("Supervised Validation", id="tab-supervised", n_clicks=0, className="tab"),
        ], className="accordion-tabs"),
        html.Div(id="performance-content")
    ])


#CHORT ANALYSIS


# --- New: Cohort Analysis Layout & Callback ---

import plotly.graph_objects as go

def build_cohort_layout():
    return html.Div([
        html.H1("📆 Cohort Retention Heatmap"),
        html.P("Analyze customer retention behavior based on first purchase month."),
        dcc.Upload(
            id='upload-cohort-data',
            children=html.Div([
                html.Span("☁️ Drag or Click to Upload CSV (same as Explore Segments data)"),
            ], className='uploader-text-icon'),
            style={'width': '100%', 'height': 'auto', 'lineHeight': '60px', 'borderWidth': '0', 'borderRadius': '15px'},
            multiple=False
        ),
        html.Hr(),
        html.Div(id="cohort-heatmap-output")
    ])


@app.callback(
    Output("cohort-heatmap-output", "children"),
    Input("upload-cohort-data", "contents"),
    State("upload-cohort-data", "filename")
)
def display_cohort_heatmap(contents, filename):
    if not contents:
        return html.Div("📁 Upload a CSV file to generate the cohort retention heatmap.")

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        # Try loading CSV (UTF-8 or fallback)
        try:
            df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        except UnicodeDecodeError:
            df = pd.read_csv(io.StringIO(decoded.decode('latin1')))
    except Exception as e:
        return html.Div(f"❌ Error reading file: {e}")

    # --- Detect date, customer, invoice columns dynamically ---
    cols = [c.lower() for c in df.columns]
    try:
        date_col = next(c for c in df.columns if 'date' in c.lower())
        customer_col = next(c for c in df.columns if 'customer' in c.lower())
        invoice_col = next(c for c in df.columns if 'invoice' in c.lower())
    except StopIteration:
        return html.Div("❌ Missing essential columns: CustomerID, InvoiceNo, InvoiceDate.")

    # Convert dates
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    df.dropna(subset=[date_col, customer_col], inplace=True)

    # --- Compute Cohort Data ---
    df['InvoiceMonth'] = df[date_col].dt.to_period('M')
    cohort_df = df.groupby(customer_col)['InvoiceMonth'].min().reset_index()
    cohort_df.columns = [customer_col, 'CohortMonth']
    df = pd.merge(df, cohort_df, on=customer_col)
    df['CohortIndex'] = (df['InvoiceMonth'].dt.year - df['CohortMonth'].dt.year) * 12 + \
                        (df['InvoiceMonth'].dt.month - df['CohortMonth'].dt.month) + 1

    cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])[customer_col].nunique().reset_index()
    cohort_pivot = cohort_data.pivot_table(index='CohortMonth', columns='CohortIndex', values=customer_col)
    cohort_size = cohort_pivot.iloc[:, 0]
    retention = cohort_pivot.divide(cohort_size, axis=0).round(3)

    # --- Plot Heatmap ---
    fig = go.Figure(data=go.Heatmap(
        z=retention.values,
        x=retention.columns.astype(str),
        y=retention.index.astype(str),
        colorscale='RdYlGn',
        hoverongaps=False
    ))

    fig.update_layout(
        title="Customer Retention by Cohort Month",
        xaxis_title="Cohort Period (Months Since First Purchase)",
        yaxis_title="Cohort Month",
        height=600,
        template="plotly_white"
    )

    return html.Div([
        html.H4(f"Cohort Heatmap for: {filename}", style={'textAlign': 'center', 'marginBottom': '10px'}),
        dcc.Graph(figure=fig)
    ])


#CHOHART ANALYSIS 
# --- Callbacks ---

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if not artifacts_loaded:
        return html.Div([html.H1("Error: Artifacts Not Found"), html.P("Please run the training scripts first.")], style={'color': 'red'})
    if pathname == "/explore-segments": return build_explore_layout()
    if pathname == "/single-prediction": return build_predict_layout()
    if pathname == "/model-performance": return build_performance_layout()
    if pathname == "/cohort-analysis": return build_cohort_layout()

    return build_overview_layout()

# NEW: Callback to toggle the sidebar
@app.callback(
    [Output("app-container", "className"),
     Output("show-sidebar-btn", "style"),
     Output("hide-sidebar-btn", "style")],
    [Input("show-sidebar-btn", "n_clicks"),
     Input("hide-sidebar-btn", "n_clicks")],
)
def toggle_sidebar(show_clicks, hide_clicks):
    ctx = dash.callback_context
    if not ctx.triggered:
        return "", {'display': 'none'}, {'display': 'block'}

    button_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
    if button_id == 'hide-sidebar-btn':
        return "sidebar-hidden", {'display': 'block'}, {'display': 'none'}
    
    return "", {'display': 'none'}, {'display': 'block'}

#starting here , new code block 2 start here 

@app.callback(
    [Output('explore-output-container', 'children'),
     Output('customer-drilldown-section', 'style'),
     Output('stored-results-data', 'data')],
    Input('upload-data', 'contents'),
    State('upload-data', 'filename')
)
def update_explore_page(contents, filename):
    if contents is None:
        return dash.no_update, {'display': 'none'}, None

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)

    try:
        # --- Handle different file types and encodings ---
        if filename.endswith('.csv'):
            try:
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
            except UnicodeDecodeError:
                df = pd.read_csv(io.StringIO(decoded.decode('latin1')))
        elif filename.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(io.BytesIO(decoded))
        else:
            return (
                html.Div(["❌ Unsupported file type. Please upload a CSV or Excel file."]),
                {'display': 'none'},
                None
            )

        # --- Perform prediction or RFM computation ---
        results = predict_segments(df)

        # --- Show message based on detected data type ---
        msg = "✅ Data loaded successfully and segmented."
        if {'InvoiceNo', 'InvoiceDate', 'CustomerID', 'Quantity', 'UnitPrice'}.issubset(set(df.columns)):
            msg = "📊 Detected raw transactional data — RFM metrics calculated automatically."

       # --- Prepare visuals or summary sections ---


        # --- Generate quick summary KPIs ---
        summary_cards = html.Div([
            html.Div([
                html.H4("🧍 Total Customers", style={'color': '#f73600'}),
                html.H3(f"{len(results):,}")
            ], className="summary-card"),
            html.Div([
                html.H4("💸 Avg Monetary Value", style={'color': '#f73600'}),
                html.H3(f"${results['Monetary'].mean():,.2f}")
            ], className="summary-card"),
            html.Div([
                html.H4("🔁 Avg Frequency", style={'color': '#f73600'}),
                html.H3(f"{results['Frequency'].mean():.2f}")
            ], className="summary-card"),
            html.Div([
                html.H4("⏰ Avg Recency", style={'color': '#f73600'}),
                html.H3(f"{results['Recency'].mean():.2f}")
            ], className="summary-card"),
            html.Div([
                html.H4("🧩 Segments Found", style={'color': '#f73600'}),
                html.H3(f"{results['Segment'].nunique()}")
            ], className="summary-card"),
        ], style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(auto-fit, minmax(180px, 1fr))',
            'gap': '20px',
            'marginBottom': '30px',
            'textAlign': 'center'
        })

        # --- Prepare visuals ---
        drilldown_style = {'display': 'block', 'marginTop': '30px'}


        #summary section ended 

        output_container = html.Div([
            html.H2("📊 Customer Segmentation Analysis", style={'textAlign': 'center', 'color': '#f73600'}),
            html.H4(f"Uploaded File: {filename}", style={'textAlign': 'center'}),
            summary_cards,
            html.P(msg, style={'color': 'green', 'textAlign': 'center'}),
            html.P(msg, style={'color': 'green', 'textAlign': 'center'}),

            # --- Add PDF download button ---
            html.Div([
                html.Button("📄 Download Report (PDF)", id='btn-download-pdf', n_clicks=0, className='button')
            ], style={'textAlign': 'center', 'marginBottom': '20px'}),

            # --- Data table ---
            dash_table.DataTable(
                data=results.to_dict('records'),
                page_size=10,
                style_header={
                    'backgroundColor': '#f73600',
                    'color': '#fff9d3',
                    'textAlign': 'center',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'center',
                    'verticalAlign': 'middle',
                    'padding': '8px'
                },
            ),

            html.Hr(),
            html.H3("📈 Visualizations", style={'textAlign': 'center'}),
            html.Div([
                #3d scater plot chart 
                dcc.Graph(
                    figure=px.pie(
                        results, 
                        names='Segment', 
                        title='Segment Distribution'
                    )
                ),
                dcc.Graph(
                    figure=px.bar(
                        results.groupby("Segment")[["Recency", "Frequency", "Monetary"]]
                        .mean().reset_index(),
                        x="Segment", 
                        y=["Recency", "Frequency", "Monetary"], 
                        barmode='group',
                        title='Average RFM Values per Segment'
                    )
                ),
                dcc.Graph(
                    figure=px.scatter_3d(
                        results,
                        x='Recency',
                        y='Frequency',
                        z='Monetary',
                        color='Segment',
                        size='Monetary',
                        title='3D Customer Segments Visualization',
                        hover_data=['Segment']
                    )
                )

                #end 3d scater plot chart 
            ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}),
        ])


        #" going to repalce for adding dowmload report option"

        return output_container, drilldown_style, results.to_json(date_format='iso', orient='split')

    except Exception as e:
        # Always return 3 values even on error
        return (
            html.Div([
                html.H3("⚠️ Error processing file", style={'color': 'red'}),
                html.P(str(e))
            ]),
            {'display': 'none'},
            None
        )

#new code blck 2  ends here
#new code block 

        output_container = html.Div([
            html.H2("📊 Customer Segmentation Analysis", style={'textAlign': 'center', 'color': '#f73600'}),
            html.H4(f"Uploaded File: {filename}", style={'textAlign': 'center'}),
            dash_table.DataTable(
                data=results.to_dict('records'),
                page_size=10,
                style_header={
                    'backgroundColor': '#f73600',
                    'color': '#fff9d3',
                    'textAlign': 'center',
                    'fontWeight': 'bold'
                },
                style_cell={
                    'textAlign': 'center',
                    'verticalAlign': 'middle',
                    'padding': '8px',
                    'whiteSpace': 'normal',
                },
            ),
            html.Br(),
            html.A(
                "⬇️ Download Segmented Data (CSV)",
                id='download-link',
                download="segmented_customers.csv",
                href="data:text/csv;charset=utf-8," + results.to_csv(index=False),
                target="_blank",
                style={
                    'display': 'block',
                    'textAlign': 'center',
                    'margin': '10px 0',
                    'fontSize': '16px',
                    'color': '#007bff'
                 }
            ),

            html.Hr(),
            html.H3("📈 Visualizations", style={'textAlign': 'center'}),
            html.Div([
                dcc.Graph(
                    figure=px.pie(results, names='Segment', title='Segment Distribution')
                ),

                dcc.Graph(
                    figure=px.bar(
                        results.groupby("Segment")[["Recency", "Frequency", "Monetary"]]
                        .mean().reset_index(),
                        x="Segment",
                        y=["Recency", "Frequency", "Monetary"],
                        barmode='group',
                        title='Average RFM Values per Segment'
                    )
                 )
            ], style={'display': 'flex', 'justifyContent': 'space-around', 'flexWrap': 'wrap'}),

            html.Div([
                 dcc.Graph(
                     figure=px.scatter(
                        results,
                        x='Recency',
                        y='Monetary',
                        color='Segment',
                        title='Customer Segments by Recency vs Monetary Value',
                        size='Frequency',
                        hover_data=['Segment']
                    )
                )
            ], style={'marginTop': '30px'}),

            html.Hr(),
            html.Div([
                html.P("Developed by kuljit kaur  | Customer Segmentation Dashboard", 
                    style={'textAlign': 'center', 'fontWeight': 'bold', 'color': '#444'}),
        
                html.P("Analyze customer behavior using RFM Model (Recency, Frequency, Monetary)",
                    style={'textAlign': 'center', 'color': '#666'}),
            ])
        ])

#end of  new code block 
        return output_container, drilldown_style, results.to_json(date_format='iso', orient='split')
    except Exception as e:
        return html.Div(['Error processing file: {}'.format(e)]), {'display': 'none'}, None

@app.callback(
    Output('customer-drilldown-section', 'children'),
    Input('stored-results-data', 'data')
)
def update_drilldown_section(jsonified_data):
    if jsonified_data is None:
        return ""

    df = pd.read_json(StringIO(jsonified_data), orient='split')

    # Try to find a column similar to 'CustomerID'
    possible_cols = ['CustomerID', 'customer_id', 'CustID', 'ID']
    customer_col = next((col for col in possible_cols if col in df.columns), None)

    if not customer_col:
        return html.Div("⚠️ No 'CustomerID' column found in your uploaded file.")

    return html.Div([
        html.H3("Customer Profile Drill-Down"),
        dcc.Dropdown(
            id='customer-dropdown',
            options=[{'label': cid, 'value': cid} for cid in df[customer_col].unique()],
            placeholder="Select a Customer ID to view details"
        ),
        html.Div(id='customer-profile-output')
    ])



@app.callback(
    Output('customer-profile-output', 'children'),
    Input('customer-dropdown', 'value'),
    State('stored-results-data', 'data')
)
def display_customer_profile(customer_id, jsonified_data):
    if not customer_id or not jsonified_data:
        return ""
    df = pd.read_json(jsonified_data, orient='split')
    customer_data = df[df['CustomerID'] == customer_id].iloc[0]
    
    recommendations = {
        "vip": "Nurture with loyalty programs and exclusive offers.",
        "low-engaged": "Re-engage with personalized discounts.",
        "churned": "Target with a win-back campaign or reduce marketing spend.",
        "Regulars": "Encourage higher frequency or spending with targeted promotions."
    }
    
    return html.Div([
        html.H4(f"Profile for Customer: {customer_id}"),
        html.P(f"Segment: {customer_data['Segment']}"),
        html.P(f"RFM Values: R={customer_data['Recency']}, F={customer_data['Frequency']}, M=${customer_data['Monetary']:.2f}"),
        html.Div(f"Recommendation: {recommendations.get(customer_data['Segment'], 'Standard engagement.')}", className="recommendation")
    ], className="profile-card")

@app.callback(
    [Output("performance-content", "children"),
     Output("tab-unsupervised", "className"),
     Output("tab-supervised", "className")],
    [Input("tab-unsupervised", "n_clicks_timestamp"),
     Input("tab-supervised", "n_clicks_timestamp")]
)
def update_performance_tabs(ts_unsupervised, ts_supervised):
    ts_unsupervised = ts_unsupervised or 0
    ts_supervised = ts_supervised or 0

    if ts_supervised > ts_unsupervised:
        report_text = "Classification report not found."
        try:
            with open("artifacts/classification_report.txt", "r") as f: report_text = f.read()
        except FileNotFoundError: pass
        content = html.Div([
            html.H3("Supervised Model Validation"),
            html.Img(src=app.get_asset_url('confusion_matrix.png'), style={'width': '50%'}),
            html.H4("Classification Report"),
            dcc.Textarea(value=report_text, readOnly=True, style={'width': '100%', 'height': 300})
        ])
        return content, "tab", "tab selected"
    else:
        content = html.Div([
            html.H3("K-Means Clustering Evaluation"),
            html.Img(src=app.get_asset_url('elbow_plot.png'), style={'width': '70%'})
        ])
        return content, "tab selected", "tab"

#older callback for simgle prediction
# @app.callback(
#     Output('prediction-output', 'children'),
#     Input('predict-button', 'n_clicks'),
#     [State('recency-input', 'value'), State('frequency-input', 'value'), State('monetary-input', 'value')]
# )


# def update_prediction_output(n_clicks, recency, frequency, monetary):
#     if n_clicks == 0: return ""
#     input_df = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
#     result = predict_segments(input_df)
#     return f"Predicted Segment: {result['Segment'][0]}"



import base64
import io
import tempfile
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import pandas as pd
from dash import Output, Input, State
import dash


@app.callback(
    Output("download-pdf", "data"),
    Input("btn-download-pdf", "n_clicks"),
    State("stored-results-data", "data"),
    prevent_initial_call=True
)
def generate_pdf_report(n_clicks, json_data):
    if not json_data:
        return dash.no_update

    # Convert JSON data back to DataFrame
    df = pd.read_json(io.StringIO(json_data), orient='split')

    # Create a temporary PDF
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    doc = SimpleDocTemplate(tmp.name)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Customer Segmentation Report", styles["Title"]))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(f"Total Customers: {len(df)}", styles["Normal"]))
    elements.append(Paragraph(f"Unique Segments: {df['Segment'].nunique()}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    for seg, sub in df.groupby("Segment"):
        avg = sub[["Recency", "Frequency", "Monetary"]].mean()
        elements.append(Paragraph(
            f"<b>Segment {seg}</b> — "
            f"Recency: {avg['Recency']:.1f}, "
            f"Frequency: {avg['Frequency']:.1f}, "
            f"Monetary: {avg['Monetary']:.1f}",
            styles["Normal"]
        ))
        elements.append(Spacer(1, 8))

    doc.build(elements)

    # ✅ Correct encoding for Dash Download
    with open(tmp.name, "rb") as f:
        encoded_pdf = base64.b64encode(f.read()).decode("utf-8")

    return {
        "content": f"data:application/pdf;base64,{encoded_pdf}",
        "filename": "Customer_Segmentation_Report.pdf",
        "type": "application/pdf",
        "base64": True
    }

#call back for live chart in single orediction 
# --- Real-time What-If Simulation Callback ---

@app.callback(
    [Output('prediction-output', 'children'),
     Output('rfm-profile-chart', 'figure')],
    [Input('recency-slider', 'value'),
     Input('frequency-slider', 'value'),
     Input('monetary-slider', 'value')]
)
def update_prediction_output(recency, frequency, monetary):
    # Build DataFrame for prediction
    input_df = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
    result = predict_segments(input_df)
    predicted_segment = result['Segment'][0]

    # Define typical RFM profiles (for radar comparison)
    profiles = {
        "VIP": [20, 30, 7000],
        "Regular": [60, 10, 2000],
        "Low-Engaged": [120, 5, 800],
        "Churned": [180, 1, 200]
    }

    import plotly.graph_objects as go
    fig = go.Figure()

    # Add all average profiles
    for seg, vals in profiles.items():
        fig.add_trace(go.Scatterpolar(
            r=vals,
            theta=["Recency", "Frequency", "Monetary"],
            fill='toself',
            name=seg,
            opacity=0.3
        ))

    # Add user input
    fig.add_trace(go.Scatterpolar(
        r=[recency, frequency, monetary],
        theta=["Recency", "Frequency", "Monetary"],
        fill='toself',
        name="Your Input",
        line=dict(color='red', width=3)
    ))

    fig.update_layout(
        title=f"RFM Profile vs Typical Segments — Predicted: {predicted_segment}",
        polar=dict(radialaxis=dict(visible=True)),
        showlegend=True
    )

    return f"🎯 Predicted Segment: {predicted_segment}", fig





# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
