import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from datetime import datetime
import os

# -----------------------------
# Load data safely
# -----------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "pink_morsels_sales.csv")

df = pd.read_csv(csv_path)

# Ensure date is datetime and sorted
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# -----------------------------
# Create line chart
# -----------------------------
fig = px.line(
    df,
    x="date",
    y="sales",
    title="Pink Morsels Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Units Sold"
    }
)

# -----------------------------
# Price increase marker (SAFE way)
# -----------------------------
price_increase_date = datetime(2021, 1, 15).timestamp()
# Vertical line (no annotation here to avoid Plotly bug)
fig.add_vline(
    x=price_increase_date,
    line_width=2,
    line_dash="dash",
    line_color="red"
)

# Separate annotation (safe)
fig.add_annotation(
    x=price_increase_date,
    y=1,
    xref="x",
    yref="paper",
    text="Price Increase (15 Jan 2021)",
    showarrow=False,
    xanchor="left",
    yanchor="bottom"
)

# -----------------------------
# Build Dash app
# -----------------------------
app = Dash(__name__)

app.layout = html.Div(
    style={"width": "80%", "margin": "auto"},
    children=[
        html.H1(
            "Impact of Pink Morsel Price Increase on Sales",
            style={"textAlign": "center"}
        ),

        html.P(
            "The red dashed line marks the Pink Morsel price increase on 15 January 2021.",
            style={"textAlign": "center"}
        ),

        dcc.Graph(figure=fig)
    ]
)

# -----------------------------
# Run server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)

