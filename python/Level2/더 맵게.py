# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    h = scoville
    while len(h) >= 2:
        a = heapq.heappop(h)
        if a >= K:
            break
        b = heapq.heappop(h)
        heapq.heappush(h, a + b*2)
        answer += 1
    if h[-1] < K:
        return -1
    return answer
