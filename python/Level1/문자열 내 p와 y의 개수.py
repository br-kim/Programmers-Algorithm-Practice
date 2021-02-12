# https://programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    counter = 0
    for i in s:
        if i == 'p':
            counter += 1
        elif i == 'y':
            counter -= 1
    return counter == 0
