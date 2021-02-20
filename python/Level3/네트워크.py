# https://programmers.co.kr/learn/courses/30/lessons/43162

def bfs(computers, des, check):
    check[des] = True
    for idx, v in enumerate(computers[des]):
        if v == 1 and idx != des and check[idx] == False:
            check = bfs(computers, idx, check)
    return check


def solution(n, computers):
    answer = 0
    check = [False] * n
    for i in range(n):
        if not check[i]:
            bfs(computers, i, check)
            answer += 1
    return answer
