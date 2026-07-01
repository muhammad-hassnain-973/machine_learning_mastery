-- 03 — JOINs and Subqueries: exercises
-- Database: ../data/sql_practice.db

-- 1. INNER JOIN — users with their orders
SELECT u.user_id, u.country, o.order_id, o.order_date
FROM users u
INNER JOIN orders o ON u.user_id = o.user_id
LIMIT 10;

-- 2. LEFT JOIN — ALL users, even those with zero orders
SELECT u.user_id, o.order_id
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
LIMIT 10;

-- 3. Classic interview pattern: users who NEVER ordered
SELECT u.user_id, u.country
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
WHERE o.order_id IS NULL;

-- 4. Three-table join — full picture: user, order, product
SELECT u.user_id, o.order_id, p.product_name, oi.quantity
FROM users u
JOIN orders o ON u.user_id = o.user_id
JOIN order_items oi ON o.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
LIMIT 10;

-- 5. Subquery — users whose total spend is above average
SELECT user_id, total_spent FROM (
    SELECT o.user_id, SUM(p.price * oi.quantity) AS total_spent
    FROM orders o
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    GROUP BY o.user_id
) t
WHERE total_spent > (
    SELECT AVG(price * quantity) FROM order_items oi2
    JOIN products p2 ON oi2.product_id = p2.product_id
);

-- ============================================================
-- Exercise: products that have NEVER been ordered
-- ============================================================
SELECT p.product_id, p.product_name
FROM products p
LEFT JOIN order_items oi ON p.product_id = oi.product_id
WHERE oi.order_item_id IS NULL;
