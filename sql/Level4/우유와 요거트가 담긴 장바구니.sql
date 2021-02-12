-- https://programmers.co.kr/learn/courses/30/lessons/62284

SELECT DISTINCT a.cart_id
FROM cart_products a
INNER JOIN cart_products b
ON a.cart_id = b.cart_id
WHERE a.name = 'Milk' and b.name = 'Yogurt'
ORDER BY a.cart_id