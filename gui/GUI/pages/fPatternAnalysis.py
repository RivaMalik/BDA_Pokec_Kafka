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
df_pcy=pd.read_csv(DATA_PATH.joinpath("const_based_pcy.csv"))
df_pcy=df_pcy.groupby("Region").filter(lambda x: len(x) == 1)

df_fpg1=pd.read_csv(DATA_PATH.joinpath("regionwise_user_pattern_fpg.csv"))
df_fpg2=pd.read_csv(DATA_PATH.joinpath("frequent_age_group_fpg.csv"))
df_fpg3=pd.read_csv(DATA_PATH.joinpath("regionwise_agegrp_fpg.csv"))

df_ar1=pd.read_csv(DATA_PATH.joinpath("neg_cor_edu_age_ar.csv"))
df_ar2=pd.read_csv(DATA_PATH.joinpath("pos_cor_edu_age_ar.csv"))
df_ar3=pd.read_csv(DATA_PATH.joinpath("edu_age_pat_ar.csv"))

json_file_path = DATA_PATH.joinpath("regions.geojson")
with open(json_file_path, encoding="utf-8") as j:
    contents= json.load(j)
    #contents = json.loads(j.read())


layout=[
                          dbc.Row(
                              dbc.Col(html.H1("Frequent Pattern Analysis",
                                              className='text-center mb-4',style={'color':"#ffffff",
                                              'marginTop': 25,
                                              'fontSize': 50 })
                                      ),style={'backgroundColor':"#1A5276"}
    ),
                          html.Br(),
                          dbc.Row([
                                   dbc.Col([
                                            html.H5("Select Algorithm"),
                                            dcc.Dropdown( id='algo-dropdown',
                                                         options=[{'label': 'Association Rules-Correlation Analysis', 'value': 'arules'},
                                                                  {'label': 'FP-Growth-Spatial Patterns', 'value': 'fp'},
                                                                  {'label': 'PCY-Constraint Based Patterns', 'value': 'pcy'}],value="fp"
                                                                  )
                                            
                                   ])
                          ]),
                          
                          html.Br(),

                          dbc.Row([
                                    dbc.Col([
                                            dcc.Graph( id='chart1'),
                                        ]),     
                                    dbc.Col([
                                            dcc.Graph( id='chart2'),
                                        ]),     
                                    dbc.Col([
                                            dcc.Graph( id='chart3'),
                                        ])                                    
                        
                          ])


                     
 
             
        
       
                          
]


@app.callback(
     [Output('chart1', 'figure'),Output('chart2', 'figure'),Output('chart3', 'figure')],

     [Input('algo-dropdown', 'value')],
    )
def update_output(value):

  if value=="pcy":
        
        vis1=df_pcy.loc[df_pcy['Region']=='Nitriansky',['EducationLevel','Region']]
        vis2=df_pcy.loc[df_pcy['Region']=='Banskobystrický',['EducationLevel','Region']]
        vis3=df_pcy.loc[df_pcy['Region']=='Prešovský',['EducationLevel','Region']]

          
        fig1 = px.choropleth(vis1, geojson=contents, color="EducationLevel",
                        locations="Region", featureidkey="properties.NM4",
                        color_discrete_sequence=px.colors.qualitative.G10,
                        projection="mercator", hover_data=["EducationLevel"]
                      )
        fig1.update_geos(fitbounds="locations", visible=False)
        fig1.update_layout(title_text="Frequent Education Pattern in Nitriansky Region")

        

        

        fig2 = px.choropleth(vis2, geojson=contents, color="EducationLevel",
                        locations="Region", featureidkey="properties.NM4",
                        color_discrete_sequence=px.colors.qualitative.Dark2,
                        projection="mercator", hover_data=["EducationLevel"]
                      )
        fig2.update_geos(fitbounds="locations", visible=False)
        fig2.update_layout(title_text="Frequent Education Pattern in Banskobystrický Region")


        fig3 = px.choropleth(vis3, geojson=contents, color="EducationLevel",
                        locations="Region", featureidkey="properties.NM4",
                        color_discrete_sequence=px.colors.qualitative.Prism,
                        projection="mercator", hover_data=["EducationLevel"]
                      )
        fig3.update_geos(fitbounds="locations", visible=False)
        fig3.update_layout(title_text="Frequent Education Pattern in Prešovský Region")

  elif value=="fp":

    fig1 = px.choropleth(df_fpg1, geojson=contents, color="% of Users",
                    locations="Region", featureidkey="properties.NM4",
                    projection="mercator", hover_data=["% of Users"]
                   )
    fig1.update_geos(fitbounds="locations", visible=False)
    fig1.update_layout(title_text="Region wise Pattern of Users")


    fig2 = px.choropleth(df_fpg2, geojson=contents, color="Age",
                    locations="Region", featureidkey="properties.NM4",
                    projection="mercator", hover_data=["Age"],
                    color_discrete_sequence=px.colors.qualitative.Bold
                   )
    fig2.update_geos(fitbounds="locations", visible=False)
    fig2.update_layout(title_text="Regional Most Frequent Age Group Pattern")


    fig3 = px.bar(df_fpg3, x="Region", y="support",
             labels=dict(support="% of User", Age="Age Group"),
             color='Age', barmode='group',
             color_discrete_sequence=px.colors.qualitative.Vivid)
    fig3.update_layout(title_text="Region wise Frequent Pattern of Different Age Groups")

  elif value=="arules":

    fig1 = px.bar(df_ar1, x="education_level", y="lift", color='age', 
             labels=dict(age="Age Group",education_level="Level of Education Completed"),
            color_discrete_sequence=px.colors.qualitative.Dark2)
    fig1.update_layout(title_text="Negative Correlation Analysis Between Education and Age")


    fig2 = px.bar(df_ar2, x="education_level", y="lift", color='age', 
          labels=dict(age="Age Group",education_level="Level of Education Completed"),
        color_discrete_sequence=px.colors.qualitative.Dark2)
    fig2.update_layout(title_text="Positive Correlation Analysis Between Education and Age")


    fig3 = px.bar(df_ar3, x="education_level", y="% of User",
             labels=dict( Age="Age Group"),
             color='age', barmode='group',
             color_discrete_sequence=px.colors.qualitative.Vivid)
    fig3.update_layout(title_text="Pattern of Education among Different Age Groups")



  return fig1,fig2,fig3
     