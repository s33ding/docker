import os
import dash
from flask import Flask
import plotly.express as px
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Create sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E', 'F'],
    'Value': [4, 3, 7, 1, 6, 4]
})

# Create the Dash app
server = Flask(__name__)

app = dash.Dash(server=server)
server=server

# Define the layout
app.layout = html.Div(children=[
    html.H1(children='Dash Plotly Example'),
    dcc.Graph(
        id='example-graph',
        figure=px.bar(data, x='Category', y='Value')
    )
])

if __name__ == '__main__':
    app.run_server()
                               
