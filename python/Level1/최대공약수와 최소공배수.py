# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    answer = []
    v_n, v_m = max(n, m), min(n, m)
    while v_m != 0:
        r = v_n % v_m
        v_n = v_m
        v_m = r
    answer.append(v_n)
    answer.append(n*m/v_n)
    return answer
