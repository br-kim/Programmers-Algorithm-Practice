-- https://programmers.co.kr/learn/courses/30/lessons/59040

SELECT animal_type, COUNT(animal_type) FROM animal_ins GROUP BY animal_type ORDER BY animal_type