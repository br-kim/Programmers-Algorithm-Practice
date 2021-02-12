# https://programmers.co.kr/learn/courses/30/lessons/12977

from itertools import combinations


def solution(nums):
    com_nums = list(combinations(nums, 3))
    answer = 0
    for i in com_nums:
        count = 0
        for j in range(1, sum(i)+1):
            if count > 2:
                break
            else:
                if sum(i) % j == 0:
                    count += 1
        else:
            if count == 2:
                answer += 1
    return answer
