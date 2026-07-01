-- 04 — Window Functions: exercises
-- Database: ../data/sql_practice.db

-- 1. ROW_NUMBER — rank each user's orders by date, most recent = 1
SELECT
    order_id, user_id, order_date,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY order_date DESC) AS recency_rank
FROM orders;

-- 2. RANK — top spender per country
SELECT
    u.country, u.user_id, SUM(p.price * oi.quantity) AS total_spent,
    RANK() OVER (PARTITION BY u.country ORDER BY SUM(p.price * oi.quantity) DESC) AS spend_rank
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
GROUP BY u.country, u.user_id;

-- 3. Running total — cumulative spend per user over time
SELECT
    user_id, order_date, order_id,
    SUM(order_total) OVER (PARTITION BY user_id ORDER BY order_date) AS running_total
FROM (
    SELECT o.order_id, o.user_id, o.order_date, SUM(p.price*oi.quantity) AS order_total
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY o.order_id, o.user_id, o.order_date
) sub;

-- 4. LAG — days since previous order (classic churn/recency feature)
SELECT
    user_id, order_date,
    order_date_num - LAG(order_date_num) OVER (PARTITION BY user_id ORDER BY order_date_num) AS days_since_last_order
FROM (
    SELECT user_id, order_date, JULIANDAY(order_date) AS order_date_num FROM orders
) t;
