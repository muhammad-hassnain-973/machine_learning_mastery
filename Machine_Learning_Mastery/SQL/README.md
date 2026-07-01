# SQL

My SQL learning log and practice queries, built while preparing for ML Engineer interviews. Focused on the 20% of SQL that shows up most in ML/data workflows: filtering, aggregation, joins, and window functions for feature engineering.

## Structure

```
SQL/
├── 01-fundamentals/          SELECT, WHERE, filtering, NULL handling, sorting
├── 02-aggregation/           GROUP BY, HAVING, CASE WHEN
├── 03-joins/                 INNER/LEFT JOIN, subqueries
├── 04-window-functions/      ROW_NUMBER, RANK, running totals, LAG
├── 05-capstone-rfm/          RFM feature engineering project (churn-style)
├── data/                     Practice database (SQLite) + CSV exports
└── resources.md              Datasets and links used for further practice
```

Each numbered folder has:
- `notes.md` — concepts covered, with the common mistakes for that topic
- `exercises.sql` — worked queries and practice exercises with answers

## Practice dataset

`data/sql_practice.db` is a small SQLite e-commerce database (`users`, `products`, `orders`, `order_items`) used throughout. `data/sql_practice_dump.sql` is a portable SQL script version (for online SQL editors), and `data/csv/` has each table as a standalone CSV.

Load it in SQLite:
```bash
sqlite3 data/sql_practice.db
```

## Capstone: RFM Feature Engineering

`05-capstone-rfm/` builds Recency, Frequency, and Monetary features per user — the standard feature set for churn prediction and customer segmentation — using CTEs and window functions. This is the piece most directly relevant to ML engineering work.

## Further practice datasets

See `resources.md` for real-world datasets (Chinook, Northwind, Olist, BigQuery public datasets) used for continued practice beyond this initial crash course.
