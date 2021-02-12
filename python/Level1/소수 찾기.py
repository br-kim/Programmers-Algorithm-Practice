# https://programmers.co.kr/learn/courses/30/lessons/12921

def solution(n):
    n = n+1
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i+i, n, i):
                sieve[j] = False
    return len([i for i in range(2, n) if sieve[i] == True])
