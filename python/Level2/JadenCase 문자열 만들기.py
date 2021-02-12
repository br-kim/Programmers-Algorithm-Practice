# https://programmers.co.kr/learn/courses/30/lessons/12951

def solution(s):
    beforeblank = True
    s = s.lower()
    answer = ""
    for i in s:
        if beforeblank and i.isalpha():
            answer += i.upper()
        else:
            answer += i
        beforeblank = False
        if i == " ":
            beforeblank = True
    return answer
