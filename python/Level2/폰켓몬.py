# https://programmers.co.kr/learn/courses/30/lessons/1845

from itertools import combinations


def solution(nums):
    nums.sort()
    arr = []
    for i in nums:
        if i not in arr:
            arr.append(i)
        if len(arr) == len(nums)//2:
            return len(arr)
    return len(arr)
