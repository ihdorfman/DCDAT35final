import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle
import base64
from tabs import tab_1, tab_2, tab_3


# Step 1. Launch the application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='UFC Judging'

logo=base64.b64encode(open('assets/logo.png', 'rb').read())

# Step 2. Create main app layout
app.layout = html.Div([
    html.Div([
        html.H4('Evaluating UFC Fight Data 1993-2019'),
        html.P("Isaac Dorfman - DCDAT35 Capstone Project")],
        style = {'padding' : '15px' ,'backgroundColor' : '#546D74'}),
    html.Br(),
    dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Scoring Criteria', value='tab-1-template'),
        dcc.Tab(label='Judge Evaluation', value='tab-2-template'),
        dcc.Tab(label='Simulated Fight', value='tab-3-template'),
    ]),
    html.Div(id='tabs-content-template')
], className='twelve columns')


# Step 3a. Create tab callback

@app.callback(Output('tabs-content-template', 'children'),
              [Input('tabs-template', 'value')])
def render_content(tab):
    if tab == 'tab-1-template':
        return tab_1.tab_1_layout
    elif tab == 'tab-2-template':
        return tab_2.tab_2_layout
    elif tab == 'tab-3-template':
        return tab_3.tab_3_layout
    elif tab == 'tab-4-template':
        return tab_4.tab_4_layout









# Step 6?. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)
