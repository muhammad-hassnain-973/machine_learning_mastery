-- Capstone — RFM Feature Engineering
-- Database: ../data/sql_practice.db

WITH order_totals AS (
    SELECT
        o.order_id, o.user_id, o.order_date,
        SUM(p.price * oi.quantity) AS order_value
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    WHERE o.status = 'completed'
    GROUP BY o.order_id, o.user_id, o.order_date
),
user_rfm AS (
    SELECT
        u.user_id,
        u.country,
        JULIANDAY('2024-12-31') - MAX(JULIANDAY(ot.order_date)) AS recency_days,
        COUNT(ot.order_id) AS frequency,
        COALESCE(SUM(ot.order_value), 0) AS monetary,
        COALESCE(AVG(ot.order_value), 0) AS avg_order_value
    FROM users u
    LEFT JOIN order_totals ot ON u.user_id = ot.user_id
    GROUP BY u.user_id, u.country
)
SELECT
    *,
    RANK() OVER (PARTITION BY country ORDER BY monetary DESC) AS spend_rank_in_country
FROM user_rfm
ORDER BY monetary DESC;
