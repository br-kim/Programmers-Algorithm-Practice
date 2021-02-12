# https://programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    res = [i for i in str(n)]
    res.sort(reverse=True)
    return int("".join(res))
