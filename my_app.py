from dash import Dash, dcc, html, Input, Output, State
import plotly.figure_factory as ff
import numpy as np

app = Dash(__name__)

app.layout = html.Div([
    html.H4("Draw Random Samples from a Normal Distribution"),
    html.Div([
        "Mean: ",
        dcc.Input(id='mean', value=0.0, type="number")
    ]),
    html.Div([
        "Std: ",
        dcc.Input(id='std', value=1.0, type="number")
    ]),
    html.Div([
        "Sample Size: ",
        dcc.Input(id='size', value=100, type="number")
    ]),
    html.Div(html.Button("Submit", id='submit', n_clicks=0)),
    dcc.Graph(id="graph"),
    html.Div(id="sample_mean"),
    html.Div(id="sample_std"),
])


@app.callback(
    Output("graph", "figure"),
    Output("sample_mean", "children"),
    Output("sample_std", "children"),
    Input("submit", "n_clicks"),
    State("mean", "value"),
    State("std", "value"),
    State("size", "value"))
def display_graph(n_clicks, mean, std, size):
    x = np.random.normal(mean, std, size)
    hist_data = [x]
    group_labels = [""]
    fig = ff.create_distplot(hist_data, group_labels)
    return fig, np.mean(x), np.std(x)


app.run_server(debug=True)