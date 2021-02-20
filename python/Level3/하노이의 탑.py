# https://programmers.co.kr/learn/courses/30/lessons/12946

def hanoi(n, from_pos, to_pos, aux_pos):
    ret = []
    if n == 1:
        ret.append([from_pos, to_pos])
        return ret
    ret.extend(hanoi(n - 1, from_pos, aux_pos, to_pos))
    ret.append([from_pos, to_pos])
    ret.extend(hanoi(n - 1, aux_pos, to_pos, from_pos))
    return ret


def solution(n):
    return hanoi(n, 1, 3, 2)
