# https://programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []
    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True
