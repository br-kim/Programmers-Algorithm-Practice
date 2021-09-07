# https://programmers.co.kr/learn/courses/30/lessons/72413


def solution(n, s, a, b, fares):
    INF = 100000 * n + 1
    board = [[INF for i in range(n)] for i in range(n)]

    for departure, destination, fare in fares:
        board[departure-1][destination-1] = fare
        board[destination-1][departure-1] = fare

    for i in range(n):
        board[i][i] = 0

    for x in range(n):
        for i in range(n):
            if i == x:
                continue

            for j in range(n):
                if i == j:
                    continue
                else:
                    board[i][j] = min(board[i][j], board[i][x] + board[x][j])

    min_value = INF
    for k in range(n):
        value = board[s-1][k] + board[k][a-1] + board[k][b-1]
        if min_value > value:
            min_value = value
    return min_value


test1 = 6, 4, 6, 2, [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
test2 = 7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
test3 = 6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [
    6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

testcase = [test1, test2, test3]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
