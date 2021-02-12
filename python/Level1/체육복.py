# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost_new = [l for l in lost if l not in reserve]
    reserve_new = [r for r in reserve if r not in lost]
    answer = n - len(lost_new)
    for l in lost_new:
        for j, r in enumerate(reserve_new):
            if r-1 <= l <= r+1:
                reserve_new[j] = -1
                answer += 1
                break
    return answer
