# https://programmers.co.kr/learn/courses/30/lessons/42889

def solution(N, stages):
    lis = [0]*(N+1)
    newlis = []
    for stage in stages:
        lis[stage-1] += 1
    remain = len(stages)
    for stage_num, cleared in enumerate(lis[:-1]):
        newlis.append([stage_num+1, cleared, remain])
        remain = remain - cleared
    newlis.sort(key=lambda x: x[1]/x[2] if x[2] != 0 else 0, reverse=True)
    return [i[0] for i in newlis]
