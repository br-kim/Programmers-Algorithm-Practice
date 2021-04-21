# https://programmers.co.kr/learn/courses/30/lessons/76501

def solution(absolutes, signs):
    answer = 0
    for a, s in zip(absolutes, signs):
        if s:
            answer += a
        else:
            answer -= a
    return answer


test1 = [4, 7, 12], [True, False, True]
test2 = [1, 2, 3], [False, False, True]

testcase = [test1, test2]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
