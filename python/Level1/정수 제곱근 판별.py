# https://programmers.co.kr/learn/courses/30/lessons/12934

def solution(n):
    n = n**0.5
    if n == int(n):
        return (n+1)**2
    return -1
