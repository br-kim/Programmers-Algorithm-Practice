# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    len_cit = len(citations)
    for i in range(len_cit):
        if i >= citations[i]:
            return i
    return len_cit
