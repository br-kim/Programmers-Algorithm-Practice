# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    divisors = []
    xy = []
    for i in range(1, yellow+1):
        if yellow % i == 0:
            divisors.append(i)

    for i in divisors[:(len(divisors)//2)+1]:
        x = max([i, yellow//i])
        y = min([i, yellow//i])
        xy.append([x, y])

    for i in xy:
        x = i[0]+2
        y = i[1]+2
        if brown+yellow == x*y:
            return [x, y]
