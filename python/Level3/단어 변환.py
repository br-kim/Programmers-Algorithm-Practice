# https://programmers.co.kr/learn/courses/30/lessons/43163

ans = 51


def is_changeable(begin, target):
    idx = 0
    change = 0
    while idx < len(begin):
        if change > 1:
            return False
        if begin[idx] != target[idx]:
            change += 1
        idx += 1
    return change == 1


def bfs(word, words, target, cnt, log):
    log = log[:]
    global ans
    if word == target and ans > cnt:
        ans = cnt
        return

    for i in words:
        if is_changeable(word, i) and i not in log:
            log.append(i)
            bfs(i, words, target, cnt+1, log)


def solution(begin, target, words):
    global ans
    if target not in words:
        return 0
    bfs(begin, words, target, 0, [])
    return ans
