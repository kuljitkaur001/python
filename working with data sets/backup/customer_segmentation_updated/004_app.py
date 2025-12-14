# src/004_app.py
# Advanced, multi-page Dash dashboard for Customer Segmentation

import dash
from dash import dcc, html, dash_table
from dash.dependencies import Input, Output, State
import pandas as pd
import joblib
from pathlib import Path
import plotly.express as px
import base64
import io

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
def predict_segments(df):
    df_copy = df.copy()
    X_scaled = artifacts["scaler"].transform(df_copy[["Recency", "Frequency", "Monetary"]])
    df_copy["Cluster"] = artifacts["kmeans_model"].predict(X_scaled)
    X_scaled_sup = artifacts["supervised_scaler"].transform(df_copy[["Recency", "Frequency", "Monetary"]])
    seg_pred = artifacts["supervised_model"].predict(X_scaled_sup)
    df_copy["Segment"] = artifacts["label_encoder"].inverse_transform(seg_pred)
    return df_copy

# --- App Layout ---
sidebar = html.Div([
    html.H2("Dashboard Navigation"), html.Hr(),
    html.P("Select a page to view"),
    html.Div([
        dcc.Link("Project Overview", href="/"),
        dcc.Link("Explore Segments", href="/explore-segments"),
        dcc.Link("Single Prediction", href="/single-prediction"),
        dcc.Link("Model Performance", href="/model-performance"),
    ], id="nav-links")
], id="sidebar")

app.layout = html.Div([dcc.Location(id="url"), sidebar, html.Div(id="page-content")], id="app-container")

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
        html.Div(
            dcc.Upload(
                id='upload-data',
                children=html.Button('Browse Files', className='button'),
                multiple=False
            ),
            className="upload-button-wrapper"
        ),
        html.Hr(),
        # Store for shared data
        dcc.Store(id='stored-results-data'),
        # Main output for charts and table
        html.Div(id='explore-output-container'),
        # Drill-down section (initially hidden)
        html.Div(id='customer-drilldown-section', style={'display': 'none'})
    ])

def build_predict_layout():
    return html.Div([
        html.H1("🔮 Single Customer Prediction"),
        html.P("Enter RFM values to get an instant segment prediction."),
        html.Div([
            html.Div([html.Label("Recency (days)"), dcc.Input(id='recency-input', type='number', value=50)]),
            html.Div([html.Label("Frequency (orders)"), dcc.Input(id='frequency-input', type='number', value=5)]),
            html.Div([html.Label("Monetary (spend)"), dcc.Input(id='monetary-input', type='number', value=1000)]),
            html.Button('Predict Segment', id='predict-button', n_clicks=0, className='button')
        ], style={'display': 'flex', 'gap': '20px', 'align-items': 'flex-end'}),
        html.Hr(),
        html.Div(id='prediction-output', style={'fontSize': 24, 'fontWeight': 'bold'})
    ])

def build_performance_layout():
    return html.Div([
        html.H1("📈 Model Performance Evaluation"),
        html.Div([
            html.Div("Unsupervised Model (K-Means)", id="tab-unsupervised", n_clicks=0, className="tab selected"),
            html.Div("Supervised Validation", id="tab-supervised", n_clicks=0, className="tab"),
        ], className="accordion-tabs"),
        html.Div(id="performance-content")
    ])

# --- Callbacks ---

@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if not artifacts_loaded:
        return html.Div([html.H1("Error: Artifacts Not Found"), html.P("Please run the training scripts first.")], style={'color': 'red'})
    if pathname == "/explore-segments": return build_explore_layout()
    if pathname == "/single-prediction": return build_predict_layout()
    if pathname == "/model-performance": return build_performance_layout()
    return build_overview_layout()

@app.callback(
    [Output('explore-output-container', 'children'),
     Output('customer-drilldown-section', 'style'),
     Output('stored-results-data', 'data')],
    Input('upload-data', 'contents'), State('upload-data', 'filename')
)
def update_explore_page(contents, filename):
    if contents is None:
        return dash.no_update, {'display': 'none'}, None

    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    try:
        df = pd.read_csv(io.StringIO(decoded.decode('utf-8')))
        results = predict_segments(df)
        
        drilldown_style = {'display': 'block', 'marginTop': '30px'}
        output_container = html.Div([
            html.H4(f"Analysis for: {filename}"),
            dash_table.DataTable(data=results.to_dict('records'), page_size=10, style_header={'backgroundColor': '#f73600', 'color': '#fff9d3'}),
            html.Hr(), html.H3("Visualizations"),
            html.Div([
                dcc.Graph(figure=px.pie(results, names='Segment', title='Segment Distribution')),
                dcc.Graph(figure=px.bar(results.groupby("Segment")[["Recency", "Frequency", "Monetary"]].mean().reset_index(), x="Segment", y=["Recency", "Frequency", "Monetary"], barmode='group'))
            ], style={'display': 'flex'}),
        ])
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
    df = pd.read_json(jsonified_data, orient='split')
    return html.Div([
        html.H3("Customer Profile Drill-Down"),
        dcc.Dropdown(
            id='customer-dropdown',
            options=[{'label': cid, 'value': cid} for cid in df['CustomerID']],
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
        # Show supervised content
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
        # Show unsupervised content (default)
        content = html.Div([
            html.H3("K-Means Clustering Evaluation"),
            html.Img(src=app.get_asset_url('elbow_plot.png'), style={'width': '70%'})
        ])
        return content, "tab selected", "tab"

@app.callback(
    Output('prediction-output', 'children'),
    Input('predict-button', 'n_clicks'),
    [State('recency-input', 'value'), State('frequency-input', 'value'), State('monetary-input', 'value')]
)
def update_prediction_output(n_clicks, recency, frequency, monetary):
    if n_clicks == 0: return ""
    input_df = pd.DataFrame([[recency, frequency, monetary]], columns=["Recency", "Frequency", "Monetary"])
    result = predict_segments(input_df)
    return f"Predicted Segment: {result['Segment'][0]}"

# --- Run the App ---
if __name__ == '__main__':
    app.run(debug=True)
