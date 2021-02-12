# https://programmers.co.kr/learn/courses/30/lessons/12926

def solution(s, n):
    # 65-90 97-122
    answer = ''
    while n > 26:
        n = n-26

    for i in s:
        if 'A' <= i <= 'Z':
            result = ord(i)+n
            if result > 90:
                result -= 26
        elif 'a' <= i <= 'z':
            result = ord(i)+n
            if result > 122:
                result -= 26
        else:
            result = 32
        answer += chr(result)
    return answer
