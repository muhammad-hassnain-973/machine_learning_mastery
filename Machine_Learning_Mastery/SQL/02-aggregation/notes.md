# 02 — Aggregation: GROUP BY, HAVING, CASE WHEN

## Concepts covered
`COUNT`, `SUM`, `AVG`, `MIN`, `MAX`, `GROUP BY`, `HAVING`, `CASE WHEN`.

## Common mistake
Confusing `WHERE` and `HAVING`.
- `WHERE` filters rows **before** grouping — it can't reference aggregates like `COUNT(*)`.
- `HAVING` filters groups **after** aggregation.

Trying `WHERE COUNT(*) > 5` throws an error — that's this rule.

`CASE WHEN` is used constantly in ML feature engineering to bucket continuous values into
categories inline (e.g. order size, spend tier, risk bucket).
