select p.product_name , sum(o.unit) as unit
FROM Orders o
JOIN Products p on p.product_id = o.product_id
WHERE o.order_date between '2020-02-01' AND '2020-02-29'
GROUP BY o.product_id
HAVING unit >= 100;