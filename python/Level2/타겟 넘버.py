# https://programmers.co.kr/learn/courses/30/lessons/43165

def dfs(idx, nums, my_sum, target):
    if idx == len(nums):
        if my_sum == target:
            return 1
        else:
            return 0
    else:
        return dfs(idx+1, nums, my_sum + nums[idx], target) + dfs(idx+1, nums, my_sum - nums[idx], target)


def solution(numbers, target):
    return dfs(0, numbers, 0, target)
