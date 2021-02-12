# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque


def solution(bridge_length, weight, truck_weights):
    answer = 0
    queue = deque()
    truck_idx = 0
    now_weight = 0
    while truck_idx < len(truck_weights):
        if now_weight+truck_weights[truck_idx] <= weight:
            queue.append([0, truck_weights[truck_idx]])
            now_weight += truck_weights[truck_idx]
            truck_idx += 1

        for i, v in enumerate(queue):
            queue[i] = [v[0]+1, v[1]]

        if queue[0][0] == bridge_length:
            passed_weight = queue.popleft()[1]
            now_weight -= passed_weight

        answer += 1
    if queue:
        answer += bridge_length
    return answer
