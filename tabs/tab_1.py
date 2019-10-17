import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

decision=base64.b64encode(open('assets/decision.png', 'rb').read())


tab_1_layout = html.Div([
    html.Div([
    html.Div([
        html.Br(),
            dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;Round winner is awarded 10 points with the round loser receiving 9 points or less."),
                dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* Scoring is first based on effective striking and/or grappling."),
                dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* The second scoring metric is effective aggressiveness in attempting to pursue a finish."),
                dcc.Markdown("&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;* The final scoring metric is fight area control; e.g. who is dictating where the fight is &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;occuring."),
        html.A('View code on github', href='https://github.com/ihdorfman/DCDAT35final'),
    ],style={'fontSize':18}, className='nine columns'),
    html.Br(),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(decision.decode()), style={'height':'300px'}),
    ],className='three columns'),


    ],className='nine columns'),

])
