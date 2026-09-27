import streamlit as st
import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
from urllib.parse import quote_plus
# Load environment variables
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
ENCODED_PASSWORD = quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql+psycopg2://{DB_USER}:{ENCODED_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)

st.set_page_config(
    page_title="DataPulse Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 DataPulse Analytics Dashboard")
st.markdown("### Sales & Customer Performance")

# Load sales data
query = "SELECT * FROM sales_data"
df = pd.read_sql(query, engine)

# -----------------------------
# FILTERS
# -----------------------------

st.sidebar.header("🔎 Filters")

selected_category = st.sidebar.multiselect(
    "Select Category",
    options=sorted(df["category"].unique()),
    default=sorted(df["category"].unique())
)

selected_status = st.sidebar.multiselect(
    "Select Status",
    options=sorted(df["status"].unique()),
    default=sorted(df["status"].unique())
)

filtered_df = df[
    (df["category"].isin(selected_category)) &
    (df["status"].isin(selected_status))
]
# -----------------------------
# KPI SECTION
# -----------------------------

total_orders = filtered_df["order_id"].nunique()
total_revenue = filtered_df["revenue"].sum()
average_order_value = filtered_df["revenue"].mean()
total_customers = filtered_df["customer_id"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Orders", total_orders)
col2.metric("Total Revenue", f"₹{total_revenue:,.2f}")
col3.metric("Average Order Value", f"₹{average_order_value:,.2f}")
col4.metric("Total Customers", total_customers)

st.divider()

# -----------------------------
# MONTHLY ORDERS
# -----------------------------

st.subheader("📅 Monthly Orders")

monthly_orders = (
    df.groupby("order_month")["order_id"]
    .nunique()
    .reset_index()
)

monthly_orders.columns = ["Month", "Orders"]

st.bar_chart(
    monthly_orders.set_index("Month")
)

# -----------------------------
# CUSTOMER REVENUE
# -----------------------------

# -----------------------------
# CUSTOMER REVENUE
# -----------------------------

st.subheader("👥 Customer Revenue")

customer_revenue = (
    filtered_df.groupby("customer_name")["revenue"]
    .sum()
    .sort_values(ascending=False)
)

st.bar_chart(customer_revenue)

# -----------------------------
# ORDER STATUS
# -----------------------------

st.subheader("📦 Order Status")

status_data = (
    filtered_df.groupby("status", as_index=False)
    .agg(
        Orders=("order_id", "nunique"),
        Revenue=("revenue", "sum")
    )
)

st.bar_chart(
    status_data,
    x="status",
    y="Orders"
)

st.dataframe(status_data)
# -----------------------------
# STATUS ANALYSIS
# -----------------------------

st.subheader("📦 Order Status")

status_data = (
    df.groupby("status", as_index=False)
    .agg(
        Orders=("order_id", "nunique"),
        Revenue=("revenue", "sum")
    )
)

st.bar_chart(
    status_data,
    x="status",
    y="Orders",
    width="stretch"
)

st.dataframe(status_data, width="stretch")
# -----------------------------
# RAW DATA
# -----------------------------

st.subheader("📋 Sales Data")

st.dataframe(filtered_df, width="stretch")