-- E-Commerce Business Analysis
-- SQLite-compatible SQL

-- 1. Monthly revenue and profit
SELECT strftime('%Y-%m', order_date) AS month,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(SUM(profit), 2) AS profit,
       COUNT(DISTINCT order_id) AS orders
FROM orders
GROUP BY month
ORDER BY month;

-- 2. Category performance
SELECT p.category,
       ROUND(SUM(o.revenue),2) AS revenue,
       ROUND(SUM(o.profit),2) AS profit,
       ROUND(SUM(o.profit)/SUM(o.revenue)*100,2) AS margin_pct
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;

-- 3. Top products by revenue
SELECT p.product_name,
       ROUND(SUM(o.revenue),2) AS revenue,
       ROUND(SUM(o.profit),2) AS profit,
       SUM(o.quantity) AS units
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name
ORDER BY revenue DESC
LIMIT 10;

-- 4. Customer segment performance
SELECT customer_segment,
       COUNT(DISTINCT order_id) AS orders,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       ROUND(SUM(revenue)/COUNT(DISTINCT order_id),2) AS aov
FROM orders
GROUP BY customer_segment
ORDER BY revenue DESC;

-- 5. City performance
SELECT city,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       COUNT(DISTINCT order_id) AS orders
FROM orders
GROUP BY city
ORDER BY revenue DESC;

-- 6. Low-margin products
SELECT p.product_name,
       ROUND(SUM(o.revenue),2) AS revenue,
       ROUND(SUM(o.profit),2) AS profit,
       ROUND(SUM(o.profit)/SUM(o.revenue)*100,2) AS margin_pct
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_id, p.product_name
HAVING SUM(o.profit)/SUM(o.revenue) < 0.15
ORDER BY margin_pct ASC;

-- 7. Discount impact
SELECT ROUND(discount*100,0) AS discount_pct,
       ROUND(SUM(revenue),2) AS revenue,
       ROUND(SUM(profit),2) AS profit,
       ROUND(SUM(profit)/SUM(revenue)*100,2) AS margin_pct
FROM orders
GROUP BY discount
ORDER BY discount;
