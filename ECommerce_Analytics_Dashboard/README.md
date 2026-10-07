# E-Commerce Analytics Dashboard

An end-to-end data analytics portfolio project built with **Python, Pandas, SQL and Streamlit**.

The project simulates an e-commerce business and turns raw order data into actionable business insights through an interactive dashboard.

## Business Questions
- How are revenue and profit trending over time?
- Which products and categories generate the most revenue?
- Which customer segments are most valuable?
- Which cities contribute the most sales?
- How do discounts affect profitability?
- Which products have weak margins?
- Are there unusual sales patterns worth investigating?

## Tech Stack
- Python
- Pandas / NumPy
- SQLite / SQL
- Streamlit
- Plotly
- Pytest

## Project Structure

```text
ECommerce_Analytics_Dashboard/
├── app.py
├── requirements.txt
├── README.md
├── data/
│   ├── orders.csv
│   └── products.csv
├── src/
│   └── analytics.py
├── sql/
│   └── business_queries.sql
└── tests/
    └── test_analytics.py
```

## Run Locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
streamlit run app.py
```

Then open the local Streamlit URL shown in the terminal.

## Key Features
1. KPI cards for revenue, profit, orders, AOV and margin.
2. Date/category/segment/city filters.
3. Monthly revenue and profit trend.
4. Category performance analysis.
5. Top-product analysis.
6. Customer segment analysis.
7. Geographic sales analysis.
8. Discount vs margin analysis.
9. Low-margin product identification.
10. CSV download of filtered data.

## Interview Talking Points

### Data Engineering
"I designed a small ETL pipeline where raw order and product CSV files are validated, joined, transformed and converted into business-level metrics."

### SQL
"I wrote analytical SQL queries using GROUP BY, CASE, JOINs, CTEs and window functions to answer business questions."

### Analytics
"I used revenue, profit, average order value and profit margin instead of looking only at sales volume."

### Product Thinking
"The dashboard is filter-driven so a business user can move from a high-level KPI to category, customer and product-level details."

## Important Note
The dataset is synthetic and created for portfolio/learning purposes. It does not represent a real company's customers or transactions.
