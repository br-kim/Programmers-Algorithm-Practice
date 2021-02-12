# https://programmers.co.kr/learn/courses/30/lessons/67257

from itertools import permutations
from collections import deque


def check_int(num):
    try:
        a = int(num)
        return True
    except:
        return False


def divide(expression):
    nums = []
    exps = []
    b = ""
    for i in expression:
        if check_int(i):
            b += i
        else:
            exps.append(i)
            nums.append(b)
            b = ""
    new_list = []
    for i in list(zip(nums, exps)):
        new_list.extend(i)
    new_list.append(b)
    return new_list


def cal(in_list):
    que = deque(in_list)
    buf = 0
    exp = in_list[1]
    if exp == '+':
        while que:
            a = que.popleft()
            if check_int(a):
                buf += int(a)
    elif exp == '-':
        b = int(que.popleft())
        while que:
            a = que.popleft()
            if check_int(a):
                b -= int(a)
        buf = b
    elif exp == '*':
        buf = 1
        while que:
            a = que.popleft()
            if check_int(a):
                buf *= int(a)
    return str(buf)


def get_exp(expression):
    my_set = set()
    for i in expression:
        if check_int(i):
            pass
        else:
            my_set.add(i)
    exps = list(permutations(list(my_set)))
    return exps


def solution(expression):
    exps = get_exp(expression)
    new_expression = divide(expression)
    ans = []
    maxv = -1
    for exp in exps:
        expression = new_expression
        for e in exp:
            buff = []
            new_exp = []
            for idx, i in enumerate(expression):
                if check_int(i):
                    buff.append(i)
                    if idx == len(expression)-1 and len(buff) > 2:
                        v = cal(buff)
                        new_exp.append(v)
                        expression = new_exp
                        buff = []
                else:
                    if i == e:
                        buff.append(i)
                    else:
                        if len(buff) > 2:
                            a = cal(buff)
                            for _ in range(len(buff)):
                                buff.pop()
                            buff.append(a)
                        buff.append(i)
                        new_exp.extend(buff)
                        buff = []
            new_exp.extend(buff)
            expression = new_exp
            if len(expression) == 1:
                value = abs(int(expression[0]))
                if value > maxv:
                    maxv = value
    return maxv
