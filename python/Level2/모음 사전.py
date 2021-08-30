# https://programmers.co.kr/learn/courses/30/lessons/84512

def solution(word):
    answer = 0
    d = {'A': 0, 'E': 1, 'I': 2, 'O': 3, 'U': 4}
    arr = [781, 156, 31, 6, 1]
    for idx, w in enumerate(word):
        answer += d[w]*arr[idx] + 1

    return answer


test1 = "AAAAE"
test2 = "AAAE"
test3 = "I"
test4 = "EIO"
testcase = [test1, test2, test3, test4]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
