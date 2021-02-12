# https://programmers.co.kr/learn/courses/30/lessons/68644

def solution(numbers):
    answer = set()
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j:
                answer.add(numbers[i]+numbers[j])
    return sorted(list(answer))
