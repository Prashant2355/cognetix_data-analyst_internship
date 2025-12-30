# Loading all prerequisite libraries
import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import plotly.graph_objects as go

# Loading & Preparing data
df = pd.read_excel("US Superstore data.xlsx")

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])
df["Delivery Days"] = (df["Ship Date"] - df["Order Date"]).dt.days

# Initializng Dash app
app = Dash(__name__)
server = app.server  # required for deployment

# Creating KPI Calculation Function
def compute_kpis(filtered_df):
    return {
        "sales": filtered_df["Sales"].sum(),
        "profit": filtered_df["Profit"].sum(),
        "orders": filtered_df["Order ID"].nunique(),
        "delivery": round(filtered_df["Delivery Days"].mean(), 2)
    }

# App Layout (Sidebar + Dashboard)
app.layout = html.Div([
    
    html.H1("Superstore Sales Dashboard", style={"textAlign": "center"}),

    html.Div([

        # 🔹 LEFT FILTER PANEL
        html.Div([
            html.H4("Filters"),

            dcc.Dropdown(
                id="region_filter",
                options=[{"label": r, "value": r} for r in df["Region"].unique()],
                multi=True,
                placeholder="Select Region"
            ),

            dcc.Dropdown(
                id="category_filter",
                options=[{"label": c, "value": c} for c in df["Category"].unique()],
                multi=True,
                placeholder="Select Category"
            ),

            dcc.Dropdown(
                id="segment_filter",
                options=[{"label": s, "value": s} for s in df["Segment"].unique()],
                multi=True,
                placeholder="Select Segment"
            ),

            dcc.DatePickerRange(
                id="date_filter",
                start_date=df["Order Date"].min(),
                end_date=df["Order Date"].max()
            )

        ], style={"width": "20%", "padding": "20px"}),

        # 🔹 MAIN DASHBOARD
        html.Div([

            # KPI CARDS
            html.Div(id="kpi_cards", style={"display": "flex", "gap": "20px"}),

            dcc.Graph(id="sales_trend"),
            dcc.Graph(id="category_sales"),
            dcc.Graph(id="region_profit"),
            dcc.Graph(id="segment_sales")

        ], style={"width": "80%"})

    ], style={"display": "flex"})

])

# Callback for (Filters + Charts + KPIs)
@app.callback(
    Output("kpi_cards", "children"),
    Output("sales_trend", "figure"),
    Output("category_sales", "figure"),
    Output("region_profit", "figure"),
    Output("segment_sales", "figure"),

    Input("region_filter", "value"),
    Input("category_filter", "value"),
    Input("segment_filter", "value"),
    Input("date_filter", "start_date"),
    Input("date_filter", "end_date"),
)
def update_dashboard(regions, categories, segments, start, end):

    filtered_df = df.copy()

    if regions:
        filtered_df = filtered_df[filtered_df["Region"].isin(regions)]
    if categories:
        filtered_df = filtered_df[filtered_df["Category"].isin(categories)]
    if segments:
        filtered_df = filtered_df[filtered_df["Segment"].isin(segments)]

    filtered_df = filtered_df[
        (filtered_df["Order Date"] >= start) &
        (filtered_df["Order Date"] <= end)
    ]

    kpi = compute_kpis(filtered_df)

    kpi_cards = [
        html.Div(f"Total Sales: {kpi['sales']:.2f}"),
        html.Div(f"Total Profit: {kpi['profit']:.2f}"),
        html.Div(f"Total Orders: {kpi['orders']}"),
        html.Div(f"Avg Delivery Days: {kpi['delivery']}")
    ]

    sales_fig = px.line(
        filtered_df.groupby("Order Date", as_index=False)["Sales"].sum(),
        x="Order Date", y="Sales", title="Sales Over Time"
    )

    cat_fig = px.bar(
        filtered_df.groupby("Category", as_index=False)["Sales"].sum(),
        x="Category", y="Sales", title="Category-wise Sales"
    )

    reg_fig = px.bar(
        filtered_df.groupby("Region", as_index=False)["Profit"].sum(),
        x="Region", y="Profit", title="Profit by Region"
    )

    seg_fig = px.bar(
        filtered_df.groupby("Segment", as_index=False)["Sales"].sum(),
        x="Segment", y="Sales", title="Segment Performance"
    )

    return kpi_cards, sales_fig, cat_fig, reg_fig, seg_fig


# Running the App (Local Publishing)
if __name__ == "__main__":
    app.run(debug=True)