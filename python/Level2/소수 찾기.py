# https://programmers.co.kr/learn/courses/30/lessons/42839

from itertools import permutations


def is_prime(num):
    cnt = 0
    for i in range(1, num//2+1):
        if num % i == 0:
            cnt += 1
        if cnt > 1:
            return False
    else:
        if cnt == 1:
            return True
        else:
            return False


def solution(numbers):
    myset = set()
    for i in range(1, len(numbers)+1):
        per = permutations(numbers, i)
        myset.update({int("".join(i)) for i in per})

    return len([i for i in myset if is_prime(i)])
