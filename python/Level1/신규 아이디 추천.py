# https://programmers.co.kr/learn/courses/30/lessons/72410

def firstPreprocess(string):
    return string.lower()


def secondPreprocess(string):
    ret = ""
    for i in string:
        if i.isalpha() or i.isdigit() or i in ["-", "_", "."]:
            ret += i
    return ret


def thirdPreprocess(string):
    stack = []
    for i in string:
        if not stack:
            stack.append(i)
        elif not (stack[-1] == '.' and i == '.'):
            stack.append(i)
    return "".join(stack)


def forthPreprocess(string):
    if string[0] == ".":
        string = string[1:]
    if string and string[-1] == ".":
        string = string[:-1]
    return string


def fifthPreprocess(string):
    if string:
        return string
    else:
        return "a"


def sixthPreprocess(string):
    if len(string) > 15:
        string = string[:15]
    if string[-1] == '.':
        string = string[:-1]
    return string


def seventhPreprocess(string):
    while len(string) < 3:
        string = string + string[-1]
    return string


def solution(new_id):
    answer = firstPreprocess(new_id)
    answer = secondPreprocess(answer)
    answer = thirdPreprocess(answer)
    answer = forthPreprocess(answer)
    answer = fifthPreprocess(answer)
    answer = sixthPreprocess(answer)
    answer = seventhPreprocess(answer)
    return answer


test1 = "...!@BaT#*..y.abcdefghijklm"
test2 = "z-+.^."
test3 = "=.="
test4 = "123_.def"
test5 = "abcdefghijklmn.p"

testcase = [test1, test2, test3, test4, test5]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
