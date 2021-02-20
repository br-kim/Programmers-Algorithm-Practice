# https://programmers.co.kr/learn/courses/30/lessons/12927

import heapq


def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))
    while n > 0:
        value = heapq.heappop(heap)[1]
        value -= 1
        heapq.heappush(heap, (-value, value))
        n -= 1
    ans = 0
    for i in heap:
        if i[1] > 0:
            ans += i[1]**2
    return ans
