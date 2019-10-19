import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import pickle
import base64

df = pd.read_pickle('data/title_fights.pkl')
title=base64.b64encode(open('assets/title.png', 'rb').read())

fight=df['fight'].values
index=df['fight'].index.values
fightlist = list(zip(index, fight))

tab_3_layout = html.Div([

    html.Div([

        html.Div([
            html.Br(),
            html.Div('Select a UFC title fight:'),
            dcc.Dropdown(
                id='page-3-dropdown',
                options=[{'label': k, 'value': i} for i,k in fightlist],
                value=fightlist[0][0]
            ),

        ],className='three columns'),

        html.Div([
            html.Br(),
            html.Div(id='page-3-content', style={'fontSize':18}),
            html.Br(),
            html.Div(id='fight-scoring',style={'fontSize':18})
        ],className='five columns'),

        html.Div([
        html.Br(),
        html.Img(src='data:image/png;base64,{}'.format(title.decode()), style={'width':'425px'}),
        ],className='four columns'),

    ],className='twelve columns'),

])
