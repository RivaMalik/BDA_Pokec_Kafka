import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import json
import pathlib





app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

intro_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Introduction", className="card-title"),
            html.P("This is data introduction"),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
,outline=True)


eda_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Exploratory Data Analysis", className="card-title"),
            html.P(
                "This card exploratory data analysis card ",
                 className="card-text"
             
            ),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
,outline=True)

fpm_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Frequent Pattern Mining", className="card-title"),
            html.P(
                "This card FPM card ",
                 className="card-text"
             
            ),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
,outline=True)

kafka_card = dbc.Card(
    dbc.CardBody(
        [
            html.H5("Parallel Computing", className="card-title"),
            html.P(
                "This card Kafka Card",
                 className="card-text"
             
            ),
            dbc.Button("Go somewhere", color="primary"),
        ]
    )
,outline=True)



app.layout=app.layout=dbc.Container([
                          dbc.Row(
                              dbc.Col(html.H1("Pokec Data Analytics",
                                              className='text-center text-primary mb-4')
                                      ),style={'backgroundColor':"#33FFE0"}
    ),
     html.Br(),
    dbc.Row([
              #dbc.Col([ html.Div("Pokec fdfdbvfhdbfvhdbvhdbfhvbhhhhhhhhhbvsdhbvhbhvbshxzcbhzsbhcvdbhvvfvfvfvfvfv")
              #],style={'backgroundColor':"#FF9C33","height": "100%"},width=3),
             
             dbc.Col([intro_card],align="start"),
             dbc.Col([eda_card],align="center"),
             dbc.Col([fpm_card],align="end")

    ],justify="around"),

                     
    html.Br(),
    html.Br(),              
        dbc.Row([
        dbc.Col([kafka_card],align="start"),
        dbc.Col([eda_card],align="center"),
        dbc.Col([fpm_card],align="end")

        ],justify="around")   
             
        
       
                          
],fluid=True)







if __name__ == '__main__':
  app.run_server(debug=True)