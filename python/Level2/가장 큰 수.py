# https://programmers.co.kr/learn/courses/30/lessons/42746

from functools import cmp_to_key


def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers.sort(key=cmp_to_key(lambda x, y: 1 if x+y < y+x else -1))
    return str(int("".join(numbers)))
