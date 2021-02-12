# https://programmers.co.kr/learn/courses/30/lessons/12913

def solution(land):
    dp = [[0 for _ in range(4)] for _ in range(len(land))]
    for i in range(4):
        dp[0][i] = land[0][i]

    for i in range(len(land)):
        for j in range(4):
            for k in range(4):
                if k != j:
                    dp[i][j] = max(dp[i][j], land[i][j] + dp[i-1][k])

    return max(dp[-1])
