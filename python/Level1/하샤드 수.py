# https://programmers.co.kr/learn/courses/30/lessons/12947

def solution(x):
    res = 0
    num = x
    while num != 0:
        res += num % 10
        num = num//10
    print(res)
    if x/res == int(x/res):
        return True
    else:
        return False
