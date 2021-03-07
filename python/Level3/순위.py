# https://programmers.co.kr/learn/courses/30/lessons/49191


def solution(n, results):
    graph = {}
    answer = 0
    for i in range(n):
        graph[i + 1] = [[], []]
    # print(graph)
    for i in results:
        win = i[0]
        lose = i[1]
        graph[lose][0].append(win)
        graph[win][1].append(lose)
    # print(graph)
    for i in range(n):
        q = [i + 1]
        visited = [i + 1]
        while q:
            now = q.pop(0)
            for _next in graph[now][0]:
                if _next not in visited:
                    q.append(_next)
                    visited.append(_next)
        # print(visited)
        q = [i + 1]
        while q:
            now = q.pop(0)
            for _next in graph[now][1]:
                if _next not in visited:
                    q.append(_next)
                    visited.append(_next)
        # print(visited)
        if len(visited) == n:
            answer += 1
    return answer


test1 = 5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
