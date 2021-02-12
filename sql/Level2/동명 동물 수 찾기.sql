-- https://programmers.co.kr/learn/courses/30/lessons/59041

SELECT name, COUNT(name) FROM animal_ins GROUP BY name HAVING COUNT(name) > 1 ORDER BY name;