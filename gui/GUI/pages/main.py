import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd


from app import app

intro_card = dbc.Card([
    dbc.CardHeader(html.H5("Introduction",className="card-title"),style={"backgroundColor":"#EE785F" }),
    dbc.CardBody(
        [
            html.P("This section provides a brief introduction to Pokec,the given data and data preprocessing"),
            dbc.Button("Explore", id="my_intro_btn", color="primary", href="/pages/introduction"),
        ]
    )
    ],outline=True)


eda_card = dbc.Card([
    dbc.CardHeader(html.H5("Exploratory Data Analysis",className="card-title"),style={"backgroundColor":"#6CD5D4" }),
    dbc.CardBody(
        [
          
            html.P(
                "This section covers the exploratory tasks and trends in data",
                 className="card-text"
             
            ),
            dbc.Button("Explore", id="my_eda_btn", color="primary", href="/pages/expDataAnalysis"),
        ]

    )
    ],outline=True)

fpm_card = dbc.Card([
    dbc.CardHeader(html.H5("Frequent Pattern Analysis",className="class-title"),style={"backgroundColor":"#F39C12" }),
    dbc.CardBody(
        [
           
            html.P(
                "This section explores the variety of frequent pattern mining tasks on data ",
                 className="card-text"
             
            ),
            dbc.Button("Explore", id="fp_btn",color="primary",href="/pages/fPatternAnalysis"),
        ]
    )
    ]
,outline=True)

kafka_card = dbc.Card(
    [
    dbc.CardHeader(html.H5("Stream Data Analysis",className="card-title"),style={"backgroundColor":"#9B529C" }),
    dbc.CardBody(
        [
          
            html.P(
                "This section explores handling of streaming data",
                 className="card-text"
                 ),
            dbc.Button("Explore", id="stm_btn", color="primary",href="/pages/streamAnalysis"),
        ]
    )
    ]
,outline=True)

asg4_card = dbc.Card(
    [
    dbc.CardHeader(html.H5("Further Analysis 1",className="card-title"),style={"backgroundColor":"#138D75" }),
    dbc.CardBody(
        [
          
            html.P(
                "This section is under development",
                 className="card-text"
                 ),
            dbc.Button("Explore", id="stm_btn", color="primary"),
        ]
    )
    ]
,outline=True)

asg5_card = dbc.Card(
    [
    dbc.CardHeader(html.H5("Further Analysis 2",className="card-title"),style={"backgroundColor":"#CB4335" }),
    dbc.CardBody(
        [
          
            html.P(
                "This section is under development",
                 className="card-text"
                 ),
            dbc.Button("Explore", id="stm_btn", color="primary"),
        ]
    )
    ]
,outline=True)



layout=[ 
                          dbc.Row(
                              dbc.Col(html.H1("Pokec Data Analytics",
                                              className='text-center mb-4',style={'color':"#ffffff",
                                              'marginTop': 25,
                                              'fontSize': 50 })
                                      ),style={'backgroundColor':"#1A5276"}
    ),
     html.Br(),
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
        dbc.Col([asg4_card],align="center"),
        dbc.Col([asg5_card],align="end")

        ],justify="around")   
             
        
       
                          
]