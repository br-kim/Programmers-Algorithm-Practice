# https://programmers.co.kr/learn/courses/30/lessons/12954

def solution(x, n):
    if x < 0:
        a = -1
    else:
        a = 1
    if x == 0:
        return [0]*n
    answer = list(range(x, x*n+a, x))
    return answer
