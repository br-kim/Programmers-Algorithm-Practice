# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    answer = phone_number[::-1]
    answer = answer[:4]+("*"*(len(phone_number)-4))
    return answer[::-1]
