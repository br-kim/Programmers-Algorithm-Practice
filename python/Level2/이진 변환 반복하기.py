# https://programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    count = 0
    del_zero_count = 0
    while s != '1':
        before = s
        after = s.count('1')
        del_zero_count += len(before)-after
        count += 1
        s = bin(after)[2:]
    return [count, del_zero_count]
