# https://programmers.co.kr/learn/courses/30/lessons/12953

def solution(arr):
    a = max(arr)
    while True:
        for i in arr:
            if a % i != 0:
                break
        else:
            return a
        a += 1
