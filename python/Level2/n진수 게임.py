# https://programmers.co.kr/learn/courses/30/lessons/17687

def nary(num, n):
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
    buffer = ""
    while num:
        buffer += str(arr[num % n])
        num = num//n
    if not buffer:
        return '0'
    return buffer[::-1]


def gen_nary_string(num, n):
    string = ""
    idx = 0
    for i in range(num):
        if i >= len(string):
            string += nary(idx, n)
            idx += 1
    return string


def solution(n, t, m, p):
    str1 = gen_nary_string(t*m, n)
    ans = ""
    for i in range(t):
        ans += str1[(m*i)+p-1]
    return ans
