SELECT customer_id, SUM(price) AS total_spent
FROM gold_orders
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
