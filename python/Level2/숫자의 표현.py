# https://programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 1
    a = range(1, n+1)
    for i in range(n+1):
        for j in range(i, n//2+2):
            total_sum = sum(a[i:j])
            if total_sum == n:
                answer += 1
                break
            if total_sum > n:
                break
    return answer
