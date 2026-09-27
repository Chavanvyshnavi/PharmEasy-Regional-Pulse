import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px

st.set_page_config(page_title="PharmEasy Dashboard")

# Connect to database
connection = sqlite3.connect("pharmeasy.db")

data = pd.read_sql_query(
    """
    SELECT order_id, order_date, region, category,
           sales_inr, profit_inr
    FROM orders_clean
    """,
    connection
)

connection.close()


data["month"] = data["order_date"].str[:7]

month_names = {
    "2026-04": "Apr 2026",
    "2026-05": "May 2026",
    "2026-06": "Jun 2026"
}

data["month"] = data["month"].map(month_names)

# Title
st.title("PharmEasy Regional Sales Dashboard")

st.write("Sales and profit analysis for April, May and June 2026.")

# Region filter
regions = ["All Regions"] + sorted(data["region"].unique())

selected_region = st.selectbox(
    "Select Region",
    regions
)

if selected_region == "All Regions":
    filtered_data = data.copy()
else:
    filtered_data = data[data["region"] == selected_region].copy()

# KPIs
total_sales = filtered_data["sales_inr"].sum()
total_profit = filtered_data["profit_inr"].sum()
total_orders = len(filtered_data)
distinct_orders = filtered_data["order_id"].nunique()

st.subheader("Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"₹{total_sales:,.2f}")
col2.metric("Total Profit", f"₹{total_profit:,.2f}")
col3.metric("Total Order Count", total_orders)
col4.metric("Distinct Orders", distinct_orders)

# Guntur finding
guntur_april = data[
    (data["region"] == "Guntur") &
    (data["month"] == "Apr 2026")
]["sales_inr"].sum()

guntur_may = data[
    (data["region"] == "Guntur") &
    (data["month"] == "May 2026")
]["sales_inr"].sum()

guntur_change = ((guntur_may - guntur_april) / guntur_april) * 100

# Category sales
category_sales = (
    filtered_data.groupby("category")["sales_inr"]
    .sum()
    .reset_index()
    .sort_values("sales_inr", ascending=False)
)

top_category = category_sales.iloc[0]["category"]

# Executive summary
st.subheader("Executive Summary")

st.write(
    f"Total sales in the selected view are ₹{total_sales:,.2f}, "
    f"with profit of ₹{total_profit:,.2f} and {total_orders:,} distinct orders. "
    f"Guntur sales increased from ₹{guntur_april:,.2f} in April to "
    f"₹{guntur_may:,.2f} in May, an increase of {guntur_change:.2f}%. "
    f"The largest category in the selected view is {top_category}. "
    f"Review the regional, category and monthly details below before taking action."
)

# Monthly sales
st.subheader("Monthly Sales")

monthly_sales = (
    filtered_data.groupby(["month", "region"])["sales_inr"]
    .sum()
    .reset_index()
)

line_chart = px.line(
    monthly_sales,
    x="month",
    y="sales_inr",
    color="region",
    markers=True,
    category_orders={
        "month": ["Apr 2026", "May 2026", "Jun 2026"]
    },
    title="How do sales change from April to June?"
)


line_chart.update_xaxes(title="Month")
line_chart.update_yaxes(
    title="Sales (INR)",
    rangemode="tozero"
)

st.plotly_chart(line_chart, use_container_width=True)

# Regional sales
st.subheader("Regional Sales")

region_sales = (
    filtered_data.groupby("region")["sales_inr"]
    .sum()
    .reset_index()
    .sort_values("sales_inr", ascending=False)
)

bar_chart = px.bar(
    region_sales,
    x="region",
    y="sales_inr",
    title="Which regions have the highest sales?"
)

bar_chart.update_xaxes(title="Region")
bar_chart.update_yaxes(
    title="Sales (INR)",
    rangemode="tozero"
)

st.plotly_chart(bar_chart, use_container_width=True)

# Category breakdown
st.subheader("Category Breakdown")

st.dataframe(
    category_sales,
    use_container_width=True
)

# Donut chart
donut_chart = px.pie(
    category_sales,
    names="category",
    values="sales_inr",
    hole=0.45,
    title="What is the sales share of each category?"
)

st.plotly_chart(donut_chart, use_container_width=True)

# Detail table
st.subheader("Region and Month Detail")

detail = (
    filtered_data.groupby(["region", "month"])
    .agg(
        sales_inr=("sales_inr", "sum"),
        profit_inr=("profit_inr", "sum"),
        order_count=("order_id", "nunique")
    )
    .reset_index()
)

st.dataframe(
    detail,
    use_container_width=True
)