import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import base64


#### DOES NOT CURRENTLY DISPLAY IMAGESS PLZ FIX ###

left=base64.b64encode(open('assets/left.png', 'rb').read())
right=base64.b64encode(open('assets/right.png', 'rb').read())

tab_4_layout = html.Div([
    html.Div([

    html.Div([
        html.Br(),
        html.Img(src='data:image/png;base64,{}'.format(left.decode()), style={'height':'425px'}),
        dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;**Red Corner**",style={'fontSize':24,'color':'Red'}),
    ],className='three columns'),


    #Sliders + Gradient
    html.Div([
        html.Br(),
        dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Head Strikes**',style={'fontSize':24}),
        dcc.Slider(
            id='head_slide',
            min=-1,
            max=1,
            step=.1,
            value=0,
            marks={
                -1:'-1',
                0:'0',
                1:'1'
            },
        ),

        html.Br(),
        dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Body Strikes**',style={'fontSize':24}),
        dcc.Slider(
            id='body_slide',
            min=-1,
            max=1,
            step=.1,
            value=0,
            marks={
                -1:'-1',
                0:'0',
                1:'1'
            },
        ),

        html.Br(),
        dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Leg Strikes**',style={'fontSize':24}),
        dcc.Slider(
            id='leg_slide',
            min=-1,
            max=1,
            step=.1,
            value=0,
            marks={
                -1:'-1',
                0:'0',
                1:'1'
            },
        ),

        html.Br(),
        dcc.Markdown('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Pass Differential**',style={'fontSize':24}),
        dcc.Slider(
            id='pass_slide',
            min=-15,
            max=15,
            step=1,
            value=0,
            marks={
                -15:'-15',
                0:'0',
                15:'15'
            },
        ),

        html.Br(),
        html.Br(),
        html.Br(),                
        html.Button(id='submit-button', n_clicks=0, children='Score'),

    ],className='three columns'),

    #Output/Results
    html.Div([
        html.Br(),
        html.Div(id='simulated-scoring',style={'fontSize':18})
    ],className='three columns'),

    html.Div([
    html.Br(),
    html.Img(src='data:image/png;base64,{}'.format(right.decode()), style={'height':'425px'}),
    dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Blue Corner**",style={'fontSize':24,'color':'Blue'}),
    ],className='three columns'),



    ],className='twelve columns'),

])
