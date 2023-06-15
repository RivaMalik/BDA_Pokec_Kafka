import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import plotly.express as px

import pandas as pd
import json
import pathlib

from app import app


#Getting path
PATH = pathlib.Path().resolve()
DATA_PATH = PATH.joinpath("data_files")


#Preparing data
df=pd.read_csv(DATA_PATH.joinpath("kafka_result_data.csv"))
fig = px.pie(df, values='count', names='user_category', title='Population of European continent')




layout=[
                          dbc.Row(
                              dbc.Col(html.H1("Stream Data Analysis",
                                              className='text-center mb-4',style={'color':"#ffffff",
                                              'marginTop': 25,
                                              'fontSize': 50 })
                                      ),style={'backgroundColor':"#1A5276"}
    ),
                          html.Br(),
             

                          dbc.Row([
                                    dbc.Col([
                                            dcc.Graph( figure=fig),
                                        ])    
                                                               
                        
                          ])


                     
 
             
        
       
                          
]


