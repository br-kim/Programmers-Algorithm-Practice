# https://programmers.co.kr/learn/courses/30/lessons/70128

def solution(a, b):
    return sum([i[0]*i[1] for i in zip(a, b)])
