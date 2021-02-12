-- https://programmers.co.kr/learn/courses/30/lessons/59044

SELECT ins.name, ins.datetime
FROM animal_ins ins
LEFT JOIN animal_outs outs
ON ins.animal_id = outs.animal_id
WHERE outs.animal_id is null
ORDER BY ins.datetime
LIMIT 3