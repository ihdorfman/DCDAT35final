import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
import pickle


compare_models = pd.read_pickle('data/compare_models.pkl')

mydata1 = go.Bar(
    x=compare_models.loc['F1 score'].index,
    y=compare_models.loc['F1 score'],
    name=compare_models.index[0],
    marker=dict(color='#332225')
)
mydata2 = go.Bar(
    x=compare_models.loc['Accuracy'].index,
    y=compare_models.loc['Accuracy'],
    name=compare_models.index[1],
    marker=dict(color='#24434C')
)
mydata3 = go.Bar(
    x=compare_models.loc['AUC score'].index,
    y=compare_models.loc['AUC score'],
    name=compare_models.index[2],
    marker=dict(color='#4c0000')
)
mylayout = go.Layout(
    title='Comparison of Judges Accuracy',
    xaxis = dict(title = 'Possible Judges'), # x-axis label
    yaxis = dict(title = 'Score'), # y-axis label

)
fig = go.Figure(data=[mydata1, mydata2, mydata3], layout=mylayout)

tab_2_layout = html.Div([
    html.Div([dcc.Graph(id = 'plot', figure = fig),],className='twelve columns')
])
