import dash
import dash_core_components as dcc
import dash_html_components as html
import base64

decision=base64.b64encode(open('assets/decision.png', 'rb').read())


tab_1_layout = html.Div([
    html.Br(),
    html.Br(),
    html.Div([
    html.Div([
        dcc.Markdown("Round winner is awarded 10 points with the round loser receiving 9 points or less."),
        dcc.Markdown("* Scoring is first based on effective striking and/or grappling."),
        dcc.Markdown("* The second scoring metric is effective aggressiveness in attempting to pursue a finish."),
        dcc.Markdown("* The final scoring metric is fight area control; e.g. who is dictating where the fight is occuring."),
        html.A('View code on github', href='https://github.com/ihdorfman/DCDAT35final'),
    ],className='nine columns'),
    html.Div([
    html.Img(src='data:image/png;base64,{}'.format(decision.decode()), style={'height':'300px'}),
    ],className='three columns'),


    ],className='nine columns'),

])
