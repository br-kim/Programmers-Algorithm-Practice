# https://programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    triangle = [[0 for i in range(j+1)] for j in range(n)]
    nums = [i for i in range(1, (n*(n+1)//2)+1)]
    di = [[1, 0], [0, 1], [-1, -1]]
    d, idx = 0, 0
    x, y = 0, -1
    while idx < len(nums):
        for _ in range(n, 0, -1):
            y += di[d][0]
            x += di[d][1]
            triangle[y][x] = nums[idx]
            idx += 1
        n -= 1
        d += 1
        d = d % 3
    answer = []
    for i in triangle:
        answer.extend(i)
    return answer
