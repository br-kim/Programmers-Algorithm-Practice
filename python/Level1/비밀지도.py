# https://programmers.co.kr/learn/courses/30/lessons/17681


def change(n):
    n = bin(n)[2:]
    res = ""
    for i in n:
        if i == "1":
            res += "#"
        else:
            res += " "
    return res


def solution(n, arr1, arr2):
    arr = []
    for i in range(len(arr1)):
        arr.append(arr1[i] | arr2[i])
    ans = []
    maxval = max(arr)
    maxlen = len(bin(maxval)[2:])
    for i in arr:
        ans.append(change(i))
    answer = []
    for i in ans:
        result = " " * (maxlen - len(i)) + i
        answer.append(result)
    return answer
