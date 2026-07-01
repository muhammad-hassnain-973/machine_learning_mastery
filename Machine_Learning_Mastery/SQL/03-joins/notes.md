# 03 — JOINs and Subqueries

## Concepts covered
`INNER JOIN`, `LEFT JOIN`, multi-table joins, basic subqueries.

## Common mistakes
1. **`INNER JOIN` when you needed `LEFT JOIN`.** `INNER JOIN` only returns rows that match
   in both tables. `LEFT JOIN` returns all rows from the left table, with `NULL` where there's
   no match. Interview questions like "find users who never ordered" require `LEFT JOIN`
   plus `WHERE right_table.id IS NULL` — using `INNER JOIN` here silently returns zero rows.

2. **Forgetting the `ON` condition** and accidentally creating a cartesian product — every row
   of table A matched with every row of table B. Always sanity-check row counts after a join.
