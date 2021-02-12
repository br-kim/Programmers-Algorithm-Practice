# https://programmers.co.kr/learn/courses/30/lessons/12985

def check(num):
    if num % 2 == 0:
        return num//2
    else:
        return (num+1)//2


def solution(n, a, b):
    answer = 1
    while True:
        if abs(a-b) == 1:
            if max(a, b) % 2 != 1:
                break
        answer += 1
        a, b = check(a), check(b)

    return answer
