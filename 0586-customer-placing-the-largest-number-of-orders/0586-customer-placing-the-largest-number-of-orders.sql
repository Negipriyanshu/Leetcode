WITH count AS (SELECT customer_number , COUNT(order_number) as order_count FROM Orders
GROUP BY customer_number 
ORDER BY order_count desc
limit 1)

SELECT customer_number FROM count

