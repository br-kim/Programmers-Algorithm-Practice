# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    dp = triangle  # [[0]*i for i in range(1,len(triangle)+1)]
    x = 1
    y = 0
    while x < len(dp):
        y = 0
        while y < len(dp[x]):
            if y == len(dp[x])-1:
                dp[x][y] = dp[x][y] + dp[x-1][y-1]
            elif y == 0:
                dp[x][y] = dp[x][y] + dp[x-1][y]
            elif 0 < y < len(dp[x]):
                dp[x][y] = max(dp[x-1][y-1], dp[x-1][y]) + dp[x][y]
            y += 1
        x += 1
    return max(dp[-1])
