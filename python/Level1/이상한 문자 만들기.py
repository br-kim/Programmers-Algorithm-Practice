# https://programmers.co.kr/learn/courses/30/lessons/12930

def solution(s):
    answer = []
    s = s.split(" ")
    for i in s:
        word = ""
        for idx, j in enumerate(i):
            if idx % 2 == 0:
                word += j.upper()
            else:
                word += j.lower()
        answer.append(word)
    return " ".join(answer)
