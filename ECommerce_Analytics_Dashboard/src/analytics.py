import pandas as pd

REQUIRED_ORDER_COLUMNS = {
    "order_id","order_date","customer_id","city","customer_segment",
    "product_id","quantity","discount","revenue","cost","profit","profit_margin"
}

def load_data(order_path="data/orders.csv", product_path="data/products.csv"):
    orders = pd.read_csv(order_path, parse_dates=["order_date"])
    products = pd.read_csv(product_path)
    missing = REQUIRED_ORDER_COLUMNS - set(orders.columns)
    if missing:
        raise ValueError(f"Missing order columns: {sorted(missing)}")
    df = orders.merge(products, on="product_id", how="left", validate="many_to_one")
    df["month"] = df["order_date"].dt.to_period("M").astype(str)
    return df

def kpis(df):
    revenue = df["revenue"].sum()
    profit = df["profit"].sum()
    orders = df["order_id"].nunique()
    aov = revenue / orders if orders else 0
    margin = profit / revenue if revenue else 0
    return {
        "revenue": revenue,
        "profit": profit,
        "orders": orders,
        "aov": aov,
        "margin": margin,
    }

def monthly_performance(df):
    return (df.groupby("month", as_index=False)
              .agg(revenue=("revenue","sum"), profit=("profit","sum"),
                   orders=("order_id","nunique"))
              .sort_values("month"))

def category_performance(df):
    return (df.groupby("category", as_index=False)
              .agg(revenue=("revenue","sum"), profit=("profit","sum"),
                   quantity=("quantity","sum"))
              .assign(margin=lambda x: x["profit"]/x["revenue"])
              .sort_values("revenue", ascending=False))

def top_products(df, n=10):
    return (df.groupby(["product_id","product_name"], as_index=False)
              .agg(revenue=("revenue","sum"), profit=("profit","sum"),
                   units=("quantity","sum"))
              .assign(margin=lambda x: x["profit"]/x["revenue"])
              .sort_values("revenue", ascending=False)
              .head(n))

def segment_performance(df):
    return (df.groupby("customer_segment", as_index=False)
              .agg(revenue=("revenue","sum"), profit=("profit","sum"),
                   orders=("order_id","nunique"))
              .assign(aov=lambda x: x["revenue"]/x["orders"])
              .sort_values("revenue", ascending=False))

def discount_analysis(df):
    out = df.copy()
    out["discount_band"] = pd.cut(
        out["discount"],
        bins=[-0.001,0,0.05,0.10,0.15,0.20],
        labels=["0%","1-5%","6-10%","11-15%","16-20%"]
    )
    return (out.groupby("discount_band", observed=False, as_index=False)
               .agg(revenue=("revenue","sum"), profit=("profit","sum"),
                    orders=("order_id","nunique"))
               .assign(margin=lambda x: x["profit"]/x["revenue"]))

def low_margin_products(df, threshold=0.15):
    p = (df.groupby(["product_id","product_name"], as_index=False)
           .agg(revenue=("revenue","sum"), profit=("profit","sum")))
    p["margin"] = p["profit"]/p["revenue"]
    return p[p["margin"] < threshold].sort_values("margin")
