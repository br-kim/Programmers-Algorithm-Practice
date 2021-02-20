# https://programmers.co.kr/learn/courses/30/lessons/42627

import heapq
from collections import deque


def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 정렬 필요
    ans = 0
    job_len = len(jobs)
    jobs = deque(jobs)
    waits = []
    now_time = 0
    while True:
        my_add = 1
        while jobs and jobs[0][0] <= now_time:
            job = jobs.popleft()
            heapq.heappush(waits, [job[1], job[0], job])

        if jobs and not waits:
            now_time += my_add
            continue

        elif not jobs and not waits:
            break

        now_job = heapq.heappop(waits)[2]
        my_add = now_job[1]
        now_time += my_add
        ans += now_time-now_job[0]

    return int(ans/job_len)
