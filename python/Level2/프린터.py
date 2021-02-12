# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque


def solution(priorities, location):
    ans = 0
    priorities = deque(priorities)
    m = max(priorities)
    while True:
        v = priorities.popleft()
        if m == v:
            ans += 1
            if location == 0:
                break
            else:
                location -= 1
            m = max(priorities)
        else:
            priorities.append(v)
            if location == 0:
                location = len(priorities) - 1
            else:
                location -= 1
    return ans
