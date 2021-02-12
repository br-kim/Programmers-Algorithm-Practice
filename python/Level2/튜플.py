# https://programmers.co.kr/learn/courses/30/lessons/64065

def solution(s):
    answer = []
    arr1 = []
    arr2 = []
    digit = []
    for i in s:
        if i.isdigit():
            digit.append(str(i))
        elif i == "," and digit:
            arr2.append(int("".join(digit)))
            digit = []
        elif i == "}" and digit:
            arr2.append(int("".join(digit)))
            arr1.append(arr2)
            arr2 = []
            digit = []
    arr1.sort(key=len)
    for i in arr1:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer
