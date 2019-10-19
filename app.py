import dash
from dash.dependencies import Input, Output, State
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pickle
import base64
from tabs import tab_1, tab_2, tab_3, tab_4


# Step 1. Launch the application
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title='UFC Judging'
app.config['suppress_callback_exceptions']=True

# Load/create assets
logo=base64.b64encode(open('assets/logo.png', 'rb').read())
df = pd.read_pickle('data/title_fights.pkl')
data = df[['pass_diff','head_diff','body_diff','leg_dif']].copy()

file = open('data/lr.pkl', 'rb')
lr = pickle.load(file)
file.close()

file = open('data/rf.pkl', 'rb')
rf = pickle.load(file)
file.close()

file = open('data/gnb.pkl', 'rb')
gnb = pickle.load(file)
file.close()

file = open('data/fitted_scaler.pkl', 'rb')
scaler = pickle.load(file)
file.close()

# Step 2. Create main app layout
app.layout = html.Div([
    html.Div([html.Div([
        html.H4('Evaluating UFC Fight Data 1993-2019'),
        html.P("Isaac Dorfman - DCDAT35 Capstone Project")],
        style = {'padding' : '15px' ,'backgroundColor' : '#546D74'}, className='nine columns'),
    html.Div([html.Img(src='data:image/png;base64,{}'.format(logo.decode()), style={'width':'265px'}),],className='three columns')],className='twelve columns'),
    html.Br(),
    html.Div([dcc.Tabs(id="tabs-template", value='tab-1-template', children=[
        dcc.Tab(label='Scoring Criteria', value='tab-1-template'),
        dcc.Tab(label='Judge Evaluation', value='tab-2-template'),
        dcc.Tab(label='Title Fights', value='tab-3-template'),
        dcc.Tab(label='Simulated Fight', value='tab-4-template'),
    ])],className='twelve columns'),
    html.Div(id='tabs-content-template')
], className='twelve columns')


# Step 3. Create tab callback

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


# Step 4. First callback for tab #3
@app.callback(Output('page-3-content', 'children'),
              [Input('page-3-dropdown', 'value')])
def page_3_dropdown(value):
    fight=df.loc[value, 'fight']
    return f"For {fight} we go to the judge's scorecards for a decision: "


# Step 5. Second calback for tab #3
@app.callback(Output('fight-scoring', 'children'),
              [Input('page-3-dropdown', 'value')])
def fight_scoring(value):
    fight_nums = data.loc[value]

    lr_pred = lr.predict([fight_nums])
    rf_pred = rf.predict([fight_nums])
    gnb_pred = gnb.predict([fight_nums])

    #Logistic regression predictions
    if lr_pred == 1:
        lr_win = df.loc[value, 'R_fighter']
    else:
        lr_win = df.loc[value, 'B_fighter']
    #Random forrest prediction
    if rf_pred == 1:
        rf_win = df.loc[value, 'R_fighter']
    else:
        rf_win = df.loc[value, 'B_fighter']
    #Gaussian Naive-Bayes prediction
    if gnb_pred == 1:
        gnb_win = df.loc[value, 'R_fighter']
    else:
        gnb_win = df.loc[value, 'B_fighter']

    if df.loc[value,'Winner'] == 0:
        actual = 'no one (hint: it was a draw)'
    else:
        actual = df.loc[value,'Winner']

    results = html.Div([
            dcc.Markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Judge Logistic Regression scores the contest for {lr_win}...'),
            html.Br(),
            dcc.Markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Judge Random Forrest scores the fight for {rf_win}...'),
            html.Br(),
            dcc.Markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Judge Gaussian Naive-Bayes scores the fight for {gnb_win}...'),
            html.Br(),
            dcc.Markdown(f'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The actual winner was {actual}.'),

    ])

    return results


#Step 6. Gradient callbacks for tab 4 ###NEVERMIND LOL###




#Step 7. Results callbacks for tab 4

@app.callback(Output('simulated-scoring', 'children'),
                    [Input('submit-button', 'n_clicks')],
                    [State('pass_slide','value'),
                    State('head_slide','value'),
                    State('body_slide','value'),
                    State('leg_slide','value'),
                    ])

def fightpicker(n_clicks,value0,value1,value2,value3):
    new_obs = [[value0,value1,value2,value3]]
    new_obs_scaled = scaler.transform(new_obs)

    lr_pred = lr.predict(new_obs_scaled)
    rf_pred = rf.predict(new_obs_scaled)
    gnb_pred = gnb.predict(new_obs_scaled)

    if lr_pred == 1:
        lr_win = 'Red'
    else:
        lr_win = 'Blue'
        #Random forrest prediction
    if rf_pred == 1:
        rf_win = 'Red'
    else:
        rf_win = 'Blue'
        #Gaussian Naive-Bayes prediction
    if gnb_pred == 1:
        gnb_win = 'Red'
    else:
        gnb_win = 'Blue'

    if sum(lr_pred + rf_pred + gnb_pred) == 1 or sum(lr_pred + rf_pred + gnb_pred) == 2:
        outcome = 'split decision'
    else:
        outcome = 'unanimous decision'

    if sum(lr_pred + rf_pred + gnb_pred) < 2:
        winner = 'Blue'
    else:
        winner = 'Red'

    results = html.Div([
            dcc.Markdown(f'Judge Logistic Regression scores the contest for {lr_win}...'),
            html.Br(),
            dcc.Markdown(f'Judge Random Forrest scores the fight for {rf_win}...'),
            html.Br(),
            dcc.Markdown(f'Judge Gaussian Naive-Bayes scores the fight for {gnb_win}...'),
            html.Br(),
            dcc.Markdown(f'Therefore the winner by {outcome} is {winner}.'),

    ])

    return results

# Step 8. Add the server clause
if __name__ == '__main__':
    app.run_server(debug = True)
