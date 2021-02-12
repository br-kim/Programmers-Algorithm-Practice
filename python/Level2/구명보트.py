# https://programmers.co.kr/learn/courses/30/lessons/42885

def solution(people, limit):
    people.sort(reverse=True)
    begin = 0
    end = len(people)-1
    answer = 0
    while begin <= end:
        if begin == end :
            answer += 1
            break
        weight_sum = people[begin] + people[end]
        if weight_sum <= limit:
            begin += 1
            end -= 1
            answer += 1
        elif weight_sum > limit:
            begin += 1
            answer += 1
    return answer