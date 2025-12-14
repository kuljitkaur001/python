# --- Prepare visuals ---
drilldown_style = {'display': 'block', 'marginTop': '30px'}

output_container = html.Div([
    html.H2("📊 Customer Segmentation Analysis", style={'textAlign': 'center', 'color': '#f73600'}),
    html.H4(f"Uploaded File: {filename}", style={'textAlign': 'center'}),
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
        dcc.Graph(figure=px.pie(results, names='Segment', title='Segment Distribution')),
        dcc.Graph(figure=px.bar(
            results.groupby("Segment")[["Recency", "Frequency", "Monetary"]]
            .mean().reset_index(),
            x="Segment", y=["Recency", "Frequency", "Monetary"], barmode='group',
            title='Average RFM Values per Segment'
        ))
    ], style={'display': 'flex', 'flexWrap': 'wrap', 'justifyContent': 'space-around'}),
])


import base64
import io
import tempfile
import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from dash import Output, Input, State
import dash

output_container = html.Div([
    html.H2("📊 Customer Segmentation Analysis", style={'textAlign': 'center', 'color': '#f73600'}),
    html.H4(f"Uploaded File: {filename}", style={'textAlign': 'center'}),
    summary_cards,
    html.P(msg, style={'color': 'green', 'textAlign': 'center'}),
