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

from app import app


#Getting path
PATH = pathlib.Path().resolve()
DATA_PATH = PATH.joinpath("data_files")


#Preparing data

df1=pd.read_csv(DATA_PATH.joinpath("age_vs_user_activity_data.csv"))
df2=pd.read_csv(DATA_PATH.joinpath("lingual_distribution.csv"))
df3=pd.read_csv(DATA_PATH.joinpath("top5_spoken_language_distribution.csv"))




layout=[ 
                          dbc.Row(
                              dbc.Col(html.H1("Exploratory Data Analysis",
                                              className='text-center mb-4',style={'color':"#ffffff",
                                              'marginTop': 25,
                                              'fontSize': 50 })
                                      ),style={'backgroundColor':"#1A5276"}
    ),
                          html.Br(),
                          dbc.Row([
                                   dbc.Col([
                                            
                                            html.H5("Select Distribution"),
                                            dcc.Dropdown( id='dist-dropdown',
                                                         options=[{'label': 'Distribution of Active and Inactive Users Among Different Age Groups', 'value': 'c1'},
                                                                  {'label': 'Distribution of Users on the Basis of Number of Languages They Speak', 'value': 'c2'},
                                                                  {'label': 'Distribution of Top 5 Languages Spoken Among Users', 'value': 'c3'}]
                                                         ,value="c1"
                                                       
                                                                  )
                                         
                                            
                                   ])
                          ]),
                          
                          html.Br(),

                          dbc.Row([
                                    dbc.Col([
                                            dcc.Graph( id='chart'),
                                        ])                            
                        
                          ])


                     
 
             
        
       
                          
]



@app.callback(
     Output('chart', 'figure'),

     [Input('dist-dropdown', 'value')],
    )
def update_output(value):

 
  if value=="c1":

    active_users=df1.query("last_login=='active'")['user_id']
    inactive_users=df1.query("last_login=='inactive'")['user_id']
    age_grp = df1['age_bin_custom_label'].unique()
    fy = active_users
    sy = inactive_users

    trace1 = go.Bar(
      x = age_grp,
      y = fy,
      name = 'Active'
    )
    trace2 = go.Bar(
      x = age_grp,
      y = sy,
      name = 'Inactive'
    )

    data = [trace1, trace2]
    layout = go.Layout(barmode = 'group')
    fig = go.Figure(data = data, layout = layout)
    fig.update_layout(
        title="Distribution of Active and Inactive Pokec Users Among Different Age Groups",
        xaxis_title="Age Group",
        yaxis_title="Number of User",

    )
        

      

  elif value=="c2":

    trace = go.Pie(labels = df2.user_category, values = df2['count'])
    data = [trace]
    fig = go.Figure(data = data,layout_title_text="Distribution of Pokec Users on the Basis of Number of Languages They Speak"
    )
 


  elif value=="c3":

    languages = df3['language']
    cnt = df3['count']
    data = [go.Bar(
          x = languages,
          y = cnt,
          marker_color=["#58D68D", "#FFC300", "#5DADE2","#B03A2E","#A569BD"]
    )]

    fig = go.Figure(data = data)
    fig.update_layout(
      title="Distribution of Top 5 Languages Spoken Among Users",
      xaxis_title="Language",
      yaxis_title="Number of User",

    )




  return fig
 
    