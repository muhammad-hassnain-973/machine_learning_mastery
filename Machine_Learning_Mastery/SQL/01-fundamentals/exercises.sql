-- 01 — Fundamentals: exercises
-- Database: ../data/sql_practice.db

-- 1. Basic select
SELECT user_id, country, referral_source FROM users LIMIT 10;

-- 2. Filter with WHERE
SELECT * FROM orders WHERE status = 'completed';

-- 3. Multiple conditions
SELECT * FROM orders WHERE status = 'completed' AND order_date >= '2024-06-01';

-- 4. NULL handling
SELECT * FROM users WHERE referral_source IS NULL;

-- 5. Pattern matching
SELECT * FROM products WHERE product_name LIKE '%Bluetooth%';

-- 6. IN / BETWEEN
SELECT * FROM users WHERE country IN ('Pakistan', 'India', 'UAE');
SELECT * FROM orders WHERE order_date BETWEEN '2024-01-01' AND '2024-03-31';

-- 7. DISTINCT
SELECT DISTINCT country FROM users;

-- 8. Sorting + limiting
SELECT * FROM orders ORDER BY order_date DESC LIMIT 5;

-- ============================================================
-- Exercise: 10 most expensive Electronics products, cheapest last
-- ============================================================
SELECT product_name, price
FROM products
WHERE category = 'Electronics'
ORDER BY price DESC
LIMIT 10;
