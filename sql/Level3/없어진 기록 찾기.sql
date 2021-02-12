-- https://programmers.co.kr/learn/courses/30/lessons/59042

SELECT animal_outs.ANIMAL_ID, animal_outs.name 
    FROM ANIMAL_INS RIGHT JOIN animal_outs
    ON animal_outs.animal_id = animal_ins.animal_id
    WHERE animal_ins.animal_id is null
    ORDER BY animal_outs.animal_id