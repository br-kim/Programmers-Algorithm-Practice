# https://programmers.co.kr/learn/courses/30/lessons/42897

def solution(money):
    dp1 = [0]*len(money)
    dp2 = [0]*len(money)

    dp1[0] = money[0]
    dp1[1] = money[0]
    for i in range(2, len(money)-1):
        dp1[i] = max(dp1[i-2]+money[i], dp1[i-1])

    answer1 = max(dp1)

    dp2[0] = 0
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-2]+money[i], dp2[i-1])

    answer2 = max(dp2)

    return max(answer1, answer2)


test1 = [1, 2, 3, 1]

testcase = [test1]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
