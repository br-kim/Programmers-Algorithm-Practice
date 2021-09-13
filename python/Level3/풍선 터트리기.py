# https://programmers.co.kr/learn/courses/30/lessons/68646


def solution(a):
    answer = [False for _ in a]
    minFront, minRear = 10**9+1, 10**9+1
    for i in range(len(a)):
        if a[i] < minFront:
            minFront = a[i]
            answer[i] = True
        if a[-1-i] < minRear:
            minRear = a[-1-i]
            answer[-1-i] = True
    return sum(answer)


test1 = [9, -1, -5]
test2 = [-16, 27, 65, -2, 58, -92, -71, -68, -61, -33]

testcase = [test1, test2]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
