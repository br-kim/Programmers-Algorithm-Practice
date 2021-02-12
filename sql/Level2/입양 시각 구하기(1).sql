-- https://programmers.co.kr/learn/courses/30/lessons/59412

SELECT date_format(datetime, '%H'), count(datetime) 
from animal_outs 
where date_format(datetime, '%H') > 8 and date_format(datetime, '%H') < 20 
group by date_format(datetime, '%H') 
order by date_format(datetime, '%H')