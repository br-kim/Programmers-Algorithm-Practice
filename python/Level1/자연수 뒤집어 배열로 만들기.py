# https://programmers.co.kr/learn/courses/30/lessons/12932

def solution(n):
    answer = []
    while n:
        answer.append(n % 10)
        n = n//10
    return answer
