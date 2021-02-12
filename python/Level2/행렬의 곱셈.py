# https://programmers.co.kr/learn/courses/30/lessons/12949

def solution(a, b):
    arr2 = []
    for i in range(len(a)):
        arr = []
        for j in range(len(b[0])):
            s = 0
            for n in range(len(a[0])):
                s += a[i][n] * b[n][j]
            arr.append(s)
        arr2.append(arr)
    return arr2
