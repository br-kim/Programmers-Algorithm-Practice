# https://programmers.co.kr/learn/courses/30/lessons/1844

from collections import deque


def solution(maps):
    visited = set()
    queue = deque([[0, 0, 1]])
    minval = len(maps[0])*len(maps)+1
    while queue:
        n = queue.popleft()
        x, y, cnt = n
        if minval <= cnt:
            break
        if (n[0], n[1]) not in visited:
            if x == len(maps[0]) - 1 and y == len(maps) - 1:
                if minval > cnt:
                    minval = cnt
            visited.add((n[0], n[1]))
            if x > 0 and maps[y][x-1] == 1:
                queue.append([x - 1, y, cnt+1])
            if y > 0 and maps[y-1][x] == 1:
                queue.append([x, y - 1, cnt+1])
            if x < len(maps[0]) - 1 and maps[y][x+1] == 1:
                queue.append([x + 1, y, cnt+1])
            if y < len(maps) - 1 and maps[y+1][x] == 1:
                queue.append([x, y+1, cnt+1])

    return minval if minval != len(maps[0]) * len(maps) + 1 else - 1


test1 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]
test2 = [[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [
    1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]
testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
