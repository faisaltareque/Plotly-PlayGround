import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()

np.random.seed(0)
r_x = np.random.randint(1, 101, 100)
r_y = np.random.randint(1, 101, 100)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure={'data': [
                                     go.Scatter(
                                         x=r_x,
                                         y=r_y,
                                         mode='markers',
                                         marker={
                                             'size': 12,
                                             'color': 'rgb(51,204,153)',
                                             'symbol': 'pentagon',
                                             'line': {'width': 2}
                                         }
                                     )],
                                     'layout': go.Layout(
                                         title='Scatterplot',
                                         xaxis={'title': 'Time'},
                                         yaxis={'title': 'Unit'}
                                     )}
                                 ), dcc.Graph(id='scatterplot2',
                                              figure={'data': [
                                                  go.Scatter(
                                                      x=r_x,
                                                      y=r_y,
                                                      mode='markers',
                                                      marker={
                                                          'size': 12,
                                                          'color': 'rgb(200,204,53)',
                                                          'symbol': 'pentagon',
                                                          'line': {'width': 2}
                                                      }
                                                  )],
                                                  'layout': go.Layout(
                                                      title='Scatterplot',
                                                      xaxis={'title': 'Time'},
                                                      yaxis={'title': 'Unit'}
                                                  )}
                                              )
                       ])

if __name__ == '__main__':
    app.run_server()
