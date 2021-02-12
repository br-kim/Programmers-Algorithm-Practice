# https://programmers.co.kr/learn/courses/30/lessons/12982

def solution(d, budget):
    answer = 0
    d.sort()
    res = 0
    for i in d:
        res += i
        if budget >= res:
            answer += 1
        else:
            return answer
    return answer
