# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    dic = {}
    for i in range(len(participant)):
        if participant[i] not in dic:
            dic[participant[i]] = 1
        else:
            dic[participant[i]] += 1
    for i in range(len(completion)):
        if completion[i] in dic:
            dic[completion[i]] -= 1
    for i in participant:
        if dic[i] != 0:
            return i
