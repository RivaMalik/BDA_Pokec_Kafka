import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output
from dash import callback_context


from app import app
from app import server
from pages import main,introduction,expDataAnalysis,fPatternAnalysis,streamAnalysis


#app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])




app.layout=dbc.Container([dcc.Location(id='url', refresh=False),
                        html.Div(id="page-content")
],fluid=True)



@app.callback(Output('page-content', 'children'),
              Input("url", "pathname")
              )
              
def loadPage(pathname):
    
    if pathname=="/pages/expDataAnalysis":
        return expDataAnalysis.layout

    elif pathname =="/pages/fPatternAnalysis":
        return fPatternAnalysis.layout  
        
    elif pathname =="/pages/introduction":
        return introduction.layout

    elif pathname =="/pages/streamAnalysis":
        return streamAnalysis.layout    
    else:
        return main.layout



if __name__ == '__main__':
    app.run_server(debug=False)