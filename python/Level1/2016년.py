# https://programmers.co.kr/learn/courses/30/lessons/12901

def solution(a, b):
    days = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    months = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    my_sum = b
    while True:
        a = a - 1
        if a < 1:
            break
        b = months[a]
        my_sum += b
    answer = days[(my_sum-1) % 7]
    return answer
