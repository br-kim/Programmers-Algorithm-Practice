# https://programmers.co.kr/learn/courses/30/lessons/12907

def solution(n, money):
    dp = [0 for _ in range(100001)]
    dp[0] = 1
    for i in range(len(money)):
        for j in range(money[i], n + 1):
            dp[j] += dp[j - money[i]]
    return dp[n]


test1 = 5, [1, 2, 5]
test2 = 10, [2, 5]

testcase = [test1, test2, ]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
