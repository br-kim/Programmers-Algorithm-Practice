# https://programmers.co.kr/learn/courses/30/lessons/12900

def solution(n):
    f1 = 0
    f2 = 1
    f3 = f1+f2
    while n > 1:
        f1 = f2
        f2 = f3
        f3 = f1+f2
        n -= 1
    return f3 % 1000000007
