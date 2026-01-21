from dash import Dash, html, dcc

app = Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1("Title"),

        dcc.Dropdown(
            id="region-picker",
            options=[
                {"label": "North", "value": "North"},
                {"label": "South", "value": "South"},
            ],
            value="North",
        ),

        dcc.Graph(
            id="visualization"
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
