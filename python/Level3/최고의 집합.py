# https://programmers.co.kr/learn/courses/30/lessons/12938

def solution(n, s):
    answer = []
    if s/n < 1:
        return [-1]
    else:
        answer = [s//n]*n
    nn = s % n
    idx = 0
    while nn > 0:
        answer[idx] += 1
        idx += 1
        nn -= 1
    return answer[::-1]
