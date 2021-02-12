# https://programmers.co.kr/learn/courses/30/lessons/68935

def ternary(n):
    result = ""
    ans = 0
    while True:
        if n == 0:
            break
        result += str(n % 3)
        n = n//3
    result = str(int(result))[::-1]
    for i in range(len(result)):
        ans += int(result[i])*(3**i)
    return ans


def solution(n):
    return ternary(n)
