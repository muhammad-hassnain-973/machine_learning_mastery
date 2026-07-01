-- 02 — Aggregation: exercises
-- Database: ../data/sql_practice.db

-- 1. Count and average
SELECT COUNT(*) AS total_orders, AVG(quantity) AS avg_qty FROM order_items;

-- 2. GROUP BY — orders per country
SELECT u.country, COUNT(o.order_id) AS num_orders
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.country
ORDER BY num_orders DESC;

-- 3. HAVING — only countries with more than 20 orders
SELECT u.country, COUNT(o.order_id) AS num_orders
FROM users u
JOIN orders o ON u.user_id = o.user_id
GROUP BY u.country
HAVING COUNT(o.order_id) > 20;

-- 4. CASE WHEN — bucket data inline
SELECT
    order_id,
    quantity,
    CASE
        WHEN quantity = 1 THEN 'single'
        WHEN quantity BETWEEN 2 AND 3 THEN 'small_batch'
        ELSE 'bulk'
    END AS order_size_bucket
FROM order_items;

-- ============================================================
-- Exercise: avg price + distinct product count per category,
-- only categories with avg price > 50
-- ============================================================
SELECT category, AVG(price) AS avg_price, COUNT(DISTINCT product_id) AS n_products
FROM products
GROUP BY category
HAVING AVG(price) > 50;
