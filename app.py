import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from pathlib import Path

st.set_page_config(page_title="Juice & Coffee Dashboard", layout="wide")

DATA_PATH = Path("data/sales_2025.csv")

def load_data(path):
    if not path.exists():
        st.warning(f"Data file not found: {path}. Run `generate_data.py` to create it.")
        return None
    df = pd.read_csv(path, parse_dates=["date"])
    df["date_only"] = df["date"].dt.date
    df["hour"] = df["date"].dt.hour
    df["weekday"] = df["date"].dt.day_name()
    df["total"] = pd.to_numeric(df["total"])
    df["quantity"] = pd.to_numeric(df["quantity"]).astype(int)
    return df

df = load_data(DATA_PATH)
if df is None:
    st.stop()

# Sidebar filters
st.sidebar.header("Filters")
min_date = df["date_only"].min()
max_date = df["date_only"].max()
date_range = st.sidebar.date_input("Date range", [min_date, max_date])
categories = st.sidebar.multiselect("Category", options=sorted(df["category"].unique()), default=sorted(df["category"].unique()))
payments = st.sidebar.multiselect("Payment method", options=sorted(df["payment_method"].unique()), default=sorted(df["payment_method"].unique()))
customers = st.sidebar.multiselect("Customer type", options=sorted(df["customer_type"].unique()), default=sorted(df["customer_type"].unique()))

mask = (
    (df["date_only"] >= date_range[0]) & (df["date_only"] <= date_range[1]) &
    (df["category"].isin(categories)) &
    (df["payment_method"].isin(payments)) &
    (df["customer_type"].isin(customers))
)
data = df.loc[mask].copy()

st.title("Juice & Coffee — Sales Dashboard")

# KPI cards
revenue = data["total"].sum()
orders = data["order_id"].nunique()
avg_order = revenue / orders if orders else 0

col1, col2, col3 = st.columns(3)
col1.metric("Revenue", f"${revenue:,.2f}")
col2.metric("Orders", f"{orders:,}")
col3.metric("Avg Order Value", f"${avg_order:,.2f}")

st.markdown("---")

# Daily sales chart
daily = data.groupby(data["date_only"]).agg(revenue=("total", "sum"), orders=("order_id", "nunique")).reset_index()
daily["date_only"] = pd.to_datetime(daily["date_only"])
fig_daily = px.line(daily, x="date_only", y="revenue", title="Daily Revenue", template="plotly_white", color_discrete_sequence=["#EF476F"])
fig_daily.update_layout(margin=dict(l=20, r=20, t=50, b=20))

# Monthly sales chart
monthly = daily.copy()
monthly["month"] = monthly["date_only"].dt.to_period("M").dt.to_timestamp()
monthly = monthly.groupby("month").agg(revenue=("revenue", "sum")).reset_index()
fig_month = px.bar(monthly, x="month", y="revenue", title="Monthly Revenue", template="plotly_white", color_discrete_sequence=["#ffd166"])

left, right = st.columns((2,1))
left.plotly_chart(fig_daily, use_container_width=True)
right.plotly_chart(fig_month, use_container_width=True)

st.markdown("---")

# Best selling items
items = data.groupby("item_name").agg(quantity=("quantity","sum"), revenue=("total","sum")).reset_index()
items = items.sort_values("quantity", ascending=False).head(10)
fig_items = px.bar(items, x="quantity", y="item_name", orientation="h", title="Top 10 Best Selling Items", template="plotly_white", color="revenue", color_continuous_scale="Teal")
st.plotly_chart(fig_items, use_container_width=True)

st.markdown("---")

# Peak hours heatmap (weekday vs hour)
pivot = data.groupby(["weekday","hour"]).agg(orders=("order_id","nunique"), revenue=("total","sum")).reset_index()
# ensure weekday order
weekday_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
pivot["weekday"] = pd.Categorical(pivot["weekday"], categories=weekday_order, ordered=True)
heat = pivot.pivot_table(index="weekday", columns="hour", values="orders", fill_value=0)
fig_heat = px.imshow(heat, labels=dict(x="Hour", y="Weekday", color="Orders"), x=heat.columns, y=heat.index, title="Peak Hours (Orders)")
st.plotly_chart(fig_heat, use_container_width=True)

st.markdown("---")

# Forecasting using Prophet
with st.expander("Sales Forecast (Prophet)"):
    try:
        from prophet import Prophet
        prophet_df = daily[["date_only","revenue"]].rename(columns={"date_only":"ds","revenue":"y"})
        m = Prophet(yearly_seasonality=True, weekly_seasonality=True, daily_seasonality=False)
        m.fit(prophet_df)
        future = m.make_future_dataframe(periods=30)
        forecast = m.predict(future)
        fig_forecast = px.line(forecast, x="ds", y=["yhat","yhat_lower","yhat_upper"], title="30-day Revenue Forecast", template="plotly_white")
        st.plotly_chart(fig_forecast, use_container_width=True)
    except Exception as e:
        st.error("Prophet is not installed or failed to run. Install requirements and try again. Error: " + str(e))

st.sidebar.markdown("---")
st.sidebar.write("Data rows: ", len(data))
