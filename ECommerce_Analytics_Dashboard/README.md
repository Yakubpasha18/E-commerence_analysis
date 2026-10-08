# E-Commerce Analytics Dashboard
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
