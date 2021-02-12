# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    answer = []
    for command in commands:
        start = command[0]-1
        end = command[1]
        index = command[2]-1
        ans = sorted(array[start:end])
        answer.append(ans[index])
    return answer
