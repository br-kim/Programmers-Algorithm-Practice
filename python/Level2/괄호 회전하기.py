# https://programmers.co.kr/learn/courses/30/lessons/76502

def is_valid(s):
    stack = []
    for i in s:
        stack.append(i)
        while len(stack) > 1:
            if ord(stack[-1]) - ord(stack[-2]) not in [1, 2]:
                break
            else:
                stack.pop()
                stack.pop()
    if stack:
        return False
    else:
        return True


def solution(s):
    answer = 0
    ori_s = s
    for r in range(len(s)):
        s = ori_s[r:]+ori_s[:r]
        if is_valid(s):
            answer += 1
    return answer


test1 = r"[](){}"
test2 = r"}]()[{"
test3 = r"[)(]"
test4 = r"}}}"
testcase = [test1, test2, test3, test4]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
