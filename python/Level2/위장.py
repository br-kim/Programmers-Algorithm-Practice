# https://programmers.co.kr/learn/courses/30/lessons/42578

def mul(lis):
    result = 1
    for i in lis:
        result *= (i+1)
    return result


def solution(clothes):
    d = dict()
    for n, v in clothes:
        if not d.get(v):
            d[v] = 1
        else:
            d[v] += 1
    return mul(d.values())-1
