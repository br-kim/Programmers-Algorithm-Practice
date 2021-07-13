# https://programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    word = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
            'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    answer = 0
    buffer = ""
    i = 0
    result = ""
    while i < len(s):
        if s[i].isalpha():
            buffer += s[i]
        else:
            result += s[i]
        if buffer in word:
            result += str(word[buffer])
            buffer = ""
        i += 1
    return int(result)


test1 = "one4seveneight"
test2 = "23four5six7"
test3 = "2three45sixseven"
test4 = "123"
testcase = [test1, test2, test3, test4]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
