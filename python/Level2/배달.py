# https://programmers.co.kr/learn/courses/30/lessons/12978

def solution(N, road, K):
    board = [[None for _ in range(N+1)] for _ in range(N+1)]
    for src, dest, cost in road:
        if board[src][dest] is None:
            board[src][dest] = cost
            board[dest][src] = cost
        else:
            if board[src][dest] > cost:
                board[src][dest] = cost
                board[dest][src] = cost
    max_val = N*10000+1
    distance = [0, 0] + [max_val for i in range(N - 1)]
    f = [1]
    while f:
        tar = f.pop(0)
        tar_adj = [t for t in range(N + 1) if board[tar][t] is not None]
        for t in tar_adj:
            if distance[t] > distance[tar] + board[t][tar]:
                distance[t] = distance[tar] + board[t][tar]
                f.append(t)

    return len([i for i in distance if i <= K])-1


test1 = 5, [[1, 2, 1], [2, 3, 3], [5, 2, 2],
            [1, 4, 2], [5, 3, 1], [5, 4, 2]], 3
test2 = 6, [[1, 2, 1], [1, 3, 2], [2, 3, 2], [
    3, 4, 3], [3, 5, 2], [3, 5, 3], [5, 6, 1]], 4

testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
