-- https://programmers.co.kr/learn/courses/30/lessons/59413

set @a := -1;
SELECT d.hour, ifnull(count(hour(datetime)),0)
FROM (SELECT @a := @a+1 as HOUR FROM ANIMAL_OUTS LIMIT 24) as d
LEFT JOIN animal_outs d2
ON d.hour = hour(datetime)
GROUP BY d.hour
ORDER BY d.hour

/*
SELECT T1.hour, ifnull(T2.count, 0)
from (
    SELECT @a := @a+1 as HOUR FROM ANIMAL_OUTS LIMIT 24) T1
left join (
    select hour(datetime) as hour, count(*) as count
    from animal_outs
    group by hour) as T2
on T2.hour = T1.hour
*/
