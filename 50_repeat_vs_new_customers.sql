-- Compare spend of repeat vs new buyers; compute multiplier (e.g., ~1.8x)
WITH first_order AS (
  SELECT customer_id, MIN(order_date) AS first_date
  FROM fact_sales
  GROUP BY 1
), orders AS (
  SELECT
    fs.customer_id,
    fs.order_id,
    fs.order_date,
    SUM(fs.quantity * fs.unit_price * (1-COALESCE(fs.discount_pct,0))) AS order_value
  FROM fact_sales fs
  GROUP BY 1,2,3
), classified AS (
  SELECT o.*, CASE WHEN o.order_date = f.first_date THEN 'NEW' ELSE 'REPEAT' END AS buyer_type
  FROM orders o
  JOIN first_order f ON f.customer_id = o.customer_id
)
SELECT
  buyer_type,
  COUNT(DISTINCT order_id)                  AS orders,
  SUM(order_value)                          AS revenue,
  AVG(order_value)                          AS avg_order_value
FROM classified
GROUP BY 1
;
