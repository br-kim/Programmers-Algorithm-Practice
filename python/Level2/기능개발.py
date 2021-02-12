# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque


def solution(p, s):
    progresses = deque(p)
    speeds = deque(s)
    answer = []
    while progresses:
        idx = 0
        ans = 0
        while idx < len(progresses):
            progresses[idx] = progresses[idx] + speeds[idx]
            idx += 1
        while progresses:
            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                ans += 1
            else:
                break
        if ans != 0:
            answer.append(ans)
    return answer
