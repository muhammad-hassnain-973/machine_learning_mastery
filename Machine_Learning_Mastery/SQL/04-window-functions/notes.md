# 04 — Window Functions

The part most crash courses skip, and the one that matters most for ML engineering — feature
engineering (recency, ranking, running totals, lag features) is a window-function problem.

## Concepts covered
`ROW_NUMBER`, `RANK`, `DENSE_RANK`, `SUM(...) OVER`, `LAG`.

## Core idea
A window function computes a value across a set of rows *related to the current row*, without
collapsing them into one row the way `GROUP BY` does.

```
FUNCTION(...) OVER (PARTITION BY col ORDER BY col)
```

- `PARTITION BY` = "reset the calculation for each group" (like `GROUP BY`, but rows aren't collapsed)
- `ORDER BY` (inside `OVER`) = the order to calculate running/ranked values in

## Common mistake
Filtering a window function result in the **same** `SELECT` it's defined in. Window functions
execute in the `SELECT` phase, which runs *after* `WHERE`. You can't do
`WHERE ROW_NUMBER() OVER (...) = 1` — you have to wrap the query in a CTE/subquery first, then
filter in the outer query.

## RANK vs DENSE_RANK vs ROW_NUMBER (interview favorite)
- `ROW_NUMBER()` — always unique, no ties, 1,2,3,4...
- `RANK()` — ties share a rank, next rank skips (1,1,3,4...)
- `DENSE_RANK()` — ties share a rank, no skip (1,1,2,3...)
