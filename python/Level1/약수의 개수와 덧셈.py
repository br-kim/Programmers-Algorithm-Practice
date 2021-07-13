# https://programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    num_range = range(left, right+1)
    answer = 0
    for i in num_range:
        if int(i**(1/2)) == i**(1/2):
            answer -= i
        else:
            answer += i
    return answer


test1 = 13, 17
test2 = 24, 27
testcase = [test1, test2]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
