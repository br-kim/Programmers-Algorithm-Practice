# https://programmers.co.kr/learn/courses/30/lessons/60058

def transfer(string):
    result = []
    for i in string:
        if i == "(":
            result.append(")")
        elif i == ")":
            result.append("(")
    return "".join(result)


def is_correct(string):
    stack = []
    for i in string:
        if i == ")":
            if not stack:
                return False
            else:
                stack.pop()
        elif i == "(":
            stack.append(i)
    if stack:
        return False
    else:
        return True


def divide(string):
    stack = []
    for idx, val in enumerate(string):
        stack.append(val)
        if stack.count("(") != 0 and stack.count("(") == stack.count(")"):
            u, v = "".join(stack), string[idx+1:]
            if is_correct(u):
                return u + divide(v)
            else:
                return '(' + divide(v) + ')' + transfer(u[1:-1])
    return ""


def solution(p):
    if is_correct(p):
        return p
    else:
        return divide(p)
