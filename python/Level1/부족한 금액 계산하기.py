# https://programmers.co.kr/learn/courses/30/lessons/82612


def solution(price, money, count):
    return max(0, ((count + 1) * count) // 2 * price - money)


test1 = 3, 20, 4
testcase = [test1]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
