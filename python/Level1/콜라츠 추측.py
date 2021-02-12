# https://programmers.co.kr/learn/courses/30/lessons/12943

def solution(num):
    counter = 0
    while counter < 500 and num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = (num*3)+1
        counter += 1
    if counter == 500:
        return -1
    return counter
