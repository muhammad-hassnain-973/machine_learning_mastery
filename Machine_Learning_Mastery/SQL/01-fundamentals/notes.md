# 01 — Fundamentals: SELECT, WHERE, Filtering

## Concepts covered
`SELECT`, `FROM`, `WHERE`, comparison/logical operators, `NULL` handling, `DISTINCT`, `ORDER BY`, `LIMIT`.

## Execution order (memorize this)
SQL is *written* as `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT`,
but it *executes* as:

```
FROM/JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

This explains most "why doesn't this work" moments later on (aliases, HAVING, window functions).

## Common mistake
Treating `NULL` like a normal value. `NULL = NULL` is **not true** — it's unknown.
Always use `IS NULL` / `IS NOT NULL`, never `= NULL`. Using `= NULL` returns zero rows
with no error, which makes it a silent, hard-to-catch bug.
