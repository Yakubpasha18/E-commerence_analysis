import streamlit as st
import pandas as pd
import plotly.express as px
from src.analytics import (
    load_data, kpis, monthly_performance, category_performance,
    top_products, segment_performance, discount_analysis, low_margin_products
)

st.set_page_config(page_title="E-Commerce Analytics", page_icon="📊", layout="wide")

st.title("📊 E-Commerce Analytics Dashboard")
st.caption("Portfolio project • Python + SQL + Pandas + Streamlit")

df = load_data()

with st.sidebar:
    st.header("Filters")
    min_date, max_date = df["order_date"].min().date(), df["order_date"].max().date()
    date_range = st.date_input("Order date", (min_date, max_date), min_value=min_date, max_value=max_date)
    categories = st.multiselect("Category", sorted(df["category"].unique()), default=sorted(df["category"].unique()))
    segments = st.multiselect("Customer segment", sorted(df["customer_segment"].unique()), default=sorted(df["customer_segment"].unique()))
    cities = st.multiselect("City", sorted(df["city"].unique()), default=sorted(df["city"].unique()))

if len(date_range) == 2:
    start, end = pd.Timestamp(date_range[0]), pd.Timestamp(date_range[1])
    filtered = df[
        (df["order_date"].between(start, end)) &
        (df["category"].isin(categories)) &
        (df["customer_segment"].isin(segments)) &
        (df["city"].isin(cities))
    ].copy()
else:
    filtered = df.iloc[0:0].copy()

if filtered.empty:
    st.warning("No data matches the selected filters.")
    st.stop()

m = kpis(filtered)
c1,c2,c3,c4,c5 = st.columns(5)
c1.metric("Revenue", f"₹{m['revenue']:,.0f}")
c2.metric("Profit", f"₹{m['profit']:,.0f}")
c3.metric("Orders", f"{m['orders']:,}")
c4.metric("AOV", f"₹{m['aov']:,.0f}")
c5.metric("Profit Margin", f"{m['margin']*100:.1f}%")

st.divider()

monthly = monthly_performance(filtered)
fig = px.line(monthly, x="month", y=["revenue","profit"], markers=True,
              title="Monthly Revenue & Profit")
fig.update_layout(legend_title_text="")
st.plotly_chart(fig, use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    cat = category_performance(filtered)
    fig = px.bar(cat, x="category", y="revenue", color="margin",
                 title="Revenue by Category", text_auto=".2s")
    st.plotly_chart(fig, use_container_width=True)

with col2:
    seg = segment_performance(filtered)
    fig = px.bar(seg, x="customer_segment", y="revenue",
                 title="Revenue by Customer Segment", text_auto=".2s")
    st.plotly_chart(fig, use_container_width=True)

col3, col4 = st.columns(2)

with col3:
    top = top_products(filtered, 10)
    fig = px.bar(top.sort_values("revenue"), x="revenue", y="product_name",
                 orientation="h", title="Top 10 Products by Revenue")
    st.plotly_chart(fig, use_container_width=True)

with col4:
    city = (filtered.groupby("city", as_index=False)
            .agg(revenue=("revenue","sum"), profit=("profit","sum"))
            .sort_values("revenue", ascending=False))
    fig = px.bar(city, x="city", y="revenue", title="Revenue by City", text_auto=".2s")
    st.plotly_chart(fig, use_container_width=True)

st.subheader("💸 Discount Impact")
disc = discount_analysis(filtered)
fig = px.bar(disc, x="discount_band", y="margin", title="Profit Margin by Discount Band",
             text_auto=".1%")
fig.update_yaxes(tickformat=".0%")
st.plotly_chart(fig, use_container_width=True)

st.subheader("⚠️ Low-Margin Products")
low = low_margin_products(filtered)
if low.empty:
    st.success("No products below the 15% margin threshold in the selected data.")
else:
    display = low.copy()
    display["margin"] = (display["margin"]*100).round(1).astype(str) + "%"
    st.dataframe(display, use_container_width=True, hide_index=True)

st.subheader("🔎 Filtered Transaction Data")
st.dataframe(
    filtered[["order_id","order_date","customer_id","city","customer_segment",
              "product_name","quantity","discount","revenue","profit","profit_margin"]],
    use_container_width=True, hide_index=True
)

csv = filtered.to_csv(index=False).encode("utf-8")
st.download_button("⬇️ Download filtered data", csv, "filtered_orders.csv", "text/csv")
