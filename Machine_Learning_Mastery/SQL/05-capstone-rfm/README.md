# Capstone — RFM Feature Engineering

RFM = **Recency, Frequency, Monetary** — a standard feature set for churn prediction,
customer segmentation, and LTV models. This is the SQL an ML engineer is realistically asked
to write, in interviews and on the job.

## Goal
One row per user with:
- `recency_days` — days since their last completed order (as of 2024-12-31)
- `frequency` — number of completed orders
- `monetary` — total amount spent
- `avg_order_value`
- `spend_rank_in_country` — this user's spend rank among users in their own country

See `query.sql` for the full implementation using CTEs and window functions.

## Extensions to try
1. Add a column bucketing users into `high_value` / `medium_value` / `low_value` using
   `CASE WHEN` on `monetary`.
2. Add a `churn_risk` flag: `1` if `recency_days > 90`, else `0`.
3. Find the top 3 highest-spending users **per country** only — note you can't filter on a
   window function in the same `SELECT` it's defined in, so wrap the whole query in a CTE and
   filter `WHERE spend_rank_in_country <= 3` in the outer query.
