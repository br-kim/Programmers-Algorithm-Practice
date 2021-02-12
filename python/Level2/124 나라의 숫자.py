# https://programmers.co.kr/learn/courses/30/lessons/12899

def solution(n):
    answer = ""
    a = ['4', '1', '2']
    while n:
        answer += a[n % 3]
        if n % 3 == 0:
            n = (n//3)-1
        else:
            n = n//3
    return answer[::-1]
