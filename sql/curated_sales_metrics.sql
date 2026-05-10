-- Aggregated sales metrics for analytics layer

WITH base AS (
    SELECT
        order_id,
        customer_id,
        order_date,
        amount,
        region
    FROM raw.orders
    WHERE order_date IS NOT NULL
),

daily_metrics AS (
    SELECT
        DATE(order_date) AS order_day,
        region,
        COUNT(DISTINCT order_id) AS total_orders,
        SUM(amount) AS total_revenue,
        AVG(amount) AS avg_order_value
    FROM base
    GROUP BY DATE(order_date), region
)

SELECT *
FROM daily_metrics;
