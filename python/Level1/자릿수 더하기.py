# https://programmers.co.kr/learn/courses/30/lessons/12931

def solution(n):
    answer = 0
    while n:
        answer += n % 10
        n = n//10
    return answer
