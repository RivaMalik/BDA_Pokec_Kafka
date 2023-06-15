import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd

from app import app





layout=[ 
                          dbc.Row(
                              dbc.Col(html.H1("Introduction",
                                              className='text-center mb-4',style={'color':"#ffffff",
                                              'marginTop': 25,
                                              'fontSize': 50 })
                                      ),style={'backgroundColor':"#1A5276"}
    ),
                          html.Br(),
                          html.Br(),

                          dbc.Row([
                                   dbc.Col([
                                            
                                            html.H4("What is Pokec?",style={'backgroundColor':"#A9CCE3"}),
                                            html.Div([
                                                "Pokec is the most popular on-line social network in Slovakia. The popularity of network has not changed even after the coming of Facebook. Pokec has been provided for more than 10 years and connects more than 1.6 million people."
                                            ],style={'backgroundColor':"#EBF5FB"})
                                            
                                   ])
                          ]),
                          
                          html.Br(),

                          dbc.Row([
                                    dbc.Col([
                                            
                                            html.H4("What does the data contain?",style={'backgroundColor':"#A9CCE3"}),
                                            html.Div([
                                                "Complete dataset of Pokec offers user profile and user relationship data. According to the requirement we only use user profile data.In its raw form it contains 1632803 records and 59 features.Most of the features are user opinions in unstructured text form."
                                            ],style={'backgroundColor':"#EBF5FB"})
                                            
                                   ])                         
                        
                          ]),
                        
                        html.Br(),

                          dbc.Row([
                                    dbc.Col([
                                            
                                            html.H4("How is Data Cleaned?",style={'backgroundColor':"#A9CCE3"}),
                                            html.Div([
                                                "Initial exploration of features indicates that the following columns contain garbage values"
                                                " fun, life_style, music, politics, cars, relationships, art_culture, hobbies_interest, science_technologies, computers_internet, education, sports, movies, travelling, health, companies_brands and more."
                                                "Apart from that we  also drop columns, mentioned below, which are not relevant for our analysis: registration,public, completion_percentage, body_type, body, my_eyesight, hair_type, sign_in_zodiac,on_pokec_i_am_looking_for."
                                                 "163 rows that contain null data in each column are also dropped. For dealing with outliers in age column we remove users with age>=100 and replace users having age=0 with median age."
                                                 "After performing the above tasks we have calculated new completion_percentage of each row."
                                                 " If the completion_percentage is less than 60% we have dropped that row. Finally we have dropped the completion_percentage column as well and saved this clean data in a csv file."
                                            ],style={'backgroundColor':"#EBF5FB"})
                                            
                                   ])                         
                        
                          ])



                     
 
             
        
       
                          
]




 
    