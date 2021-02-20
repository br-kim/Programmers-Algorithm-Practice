# https://programmers.co.kr/learn/courses/30/lessons/43238

def solution(n, times):
    answer = 0
    lo = 0
    hi = n*max(times)
    answer = hi
    while lo <= hi:
        mid = (lo+hi)//2
        ans = 0
        for i in times:
            ans += mid//i
        if n > ans:
            lo = mid+1
        else:
            if mid <= answer:
                answer = mid
            hi = mid-1
    return answer
