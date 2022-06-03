import pandas as pd 
import dash 
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, output

dcc.Dropdown(id='input = type',
                options=[
                        ('label',:'Yearly Airline Performance Report','value':'Opt1'), 
                        ('label':'Yearly Airline Delay Report', 'value':'Opt2')


                        placeholder = 'select a report type',style={centre})  

output(component_id='plotly1',component_property='children'),
output(plot2),
output(plot2),
output(plot4),
output(plot5)]

line_fig =px.(line_data, x='month', y='AirTime', color='reporting_Airline',title='Average monthly flight time (minutes) by airlines')

tree_fig = px.treemap(data.path=['DestState','Reporting_Airlines'],
                           values = 'Flights',
                           color='Flights',
                           color_continuous_scale='RdBu'],
                           title='Flight count by airlines to destruction state'

app.layout=(html.Div(children=html.H1(Airline Dashboard',style={'textAlign':'center' 'color','#503036', 'font-size':24}
                                                                   [html.P('proportion of distance group(250 mile distance internal group) by flight', style=(
                                                                              
                                                                                                                                        dcc.Graph(figure=fig).

        ])

#Run the application
if ___name___=='main'___':
    app[.run_server()]





                                                                                            