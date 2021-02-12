-- https://programmers.co.kr/learn/courses/30/lessons/59043

SELECT ins.animal_id, outs.name
FROM animal_ins ins
INNER JOIN animal_outs outs
ON ins.animal_id = outs.animal_id
WHERE ins.datetime > outs.datetime
ORDER BY ins.datetime