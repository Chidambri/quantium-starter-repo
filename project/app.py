from dash import Dash, dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Sample data (replace with your real dataset)
df = pd.DataFrame({
    "date": pd.date_range("2023-01-01", periods=12, freq="ME"),
    "sales": [120, 150, 170, 160, 180, 200, 210, 195, 220, 230, 250, 270],
    "region": ["north", "south", "east", "west"] * 3
})

app = Dash(__name__)
app.title = "Pink Morsels Sales Visualiser"

app.layout = html.Div(
    className="container",
    children=[
        html.H1("Pink Morsels Regional Sales", className="title"),

        html.Div(
            className="controls",
            children=[
                html.Label("Select Region:", className="label"),
                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    className="radio-items"
                ),
            ]
        ),

        dcc.Graph(id="sales-line-chart", className="chart"),
    ]
)

@app.callback(
    Output("sales-line-chart", "figure"),
    Input("region-radio", "value")
)
def update_chart(selected_region):
    if selected_region == "all":
        filtered_df = df
    else:
        filtered_df = df[df["region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales",
        color="region",
        markers=True,
        title="Pink Morsels Sales Over Time"
    )

    fig.update_layout(
        template="plotly_white",
        title_x=0.5
    )

    return fig
