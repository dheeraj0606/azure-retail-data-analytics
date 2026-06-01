# KPI Definitions – Retail Analytics

## 1. Total Revenue
SUM(order_amount)

## 2. Total Orders
COUNT(DISTINCT order_id)

## 3. Average Order Value (AOV)
SUM(order_amount) / COUNT(DISTINCT order_id)

## 4. Customer Retention Rate
Returning Customers / Total Customers

## 5. Revenue by Region
SUM(order_amount) GROUP BY region

## 6. Daily Active Customers
COUNT(DISTINCT customer_id) per day
