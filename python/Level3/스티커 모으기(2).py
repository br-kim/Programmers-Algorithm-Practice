# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    if len(sticker) < 3:
        return max(sticker)
    dp1 = [0]*len(sticker)
    dp2 = [0]*len(sticker)

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]
    for i in range(2, len(sticker)-1):
        dp1[i] = max(dp1[i-2]+sticker[i], dp1[i-1])

    answer1 = max(dp1)

    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, len(sticker)):
        dp2[i] = max(dp2[i-2]+sticker[i], dp2[i-1])

    answer2 = max(dp2)

    return max(answer1, answer2)


test1 = [14, 6, 5, 11, 3, 9, 2, 10]
test2 = [1, 3, 2, 5, 4]

testcase = [test1, test2]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
