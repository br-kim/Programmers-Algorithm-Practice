# https://programmers.co.kr/learn/courses/30/lessons/42898

def rec(row, col, dp):
    if row < 1 or col < 1 or dp[row][col] < 0:
        return 0
    if dp[row][col] > 0:
        return dp[row][col]
    dp[row][col] = rec(row, col-1, dp) + rec(row-1, col, dp)
    return dp[row][col]


def solution(m, n, puddles):
    dp = [[0 for i in range(m+1)] for j in range(n+1)]
    for i in puddles:
        dp[i[1]][i[0]] = -1
    dp[1][1] = 1
    return rec(n, m, dp) % 1000000007
