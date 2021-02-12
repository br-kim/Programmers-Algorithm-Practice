# https://programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    idx = 0
    stack = []
    while idx < len(words):
        num = (idx % n)+1
        turn = (idx//n)+1
        if words[idx] in stack:
            return [num, turn]

        if idx > 0 and words[idx][0] != words[idx-1][-1]:
            return [num, turn]

        stack.append(words[idx])
        idx += 1
    else:
        return [0, 0]
