# https://programmers.co.kr/learn/courses/30/lessons/60063

from collections import deque


def can_moves(coord, board):
    direction = [1, 0], [-1, 0], [0, 1], [0, -1]
    moves = []
    robot1, robot2 = coord
    # 상하좌우 이동
    for dx, dy in direction:
        xy1 = (robot1[0] + dy, robot1[1] + dx)
        xy2 = (robot2[0] + dy, robot2[1] + dx)
        if board[xy1[0]][xy1[1]] == 0 and board[xy2[0]][xy2[1]] == 0:
            moves.append((xy1, xy2))
    # 회전
    if robot1[0] == robot2[0]:  # 로봇 2칸의 Y값이 같을 때(가로)
        for d in (-1, 1):  # -1이 비어있으면 아래, 1이 비어있으면 위로 회전 가능
            if board[robot1[0]+d][robot1[1]] == 0 and board[robot2[0]+d][robot2[1]] == 0:
                moves.append((robot1, (robot1[0]+d, robot1[1])))
                moves.append((robot2, (robot2[0]+d, robot2[1])))
    else:  # 로봇 2칸의 X값이 같을 때(세로)
        for d in (-1, 1):  # -1이 비어있으면 왼쪽, 1이 비어있으면 오른쪽으로 회전 가능
            if board[robot1[0]][robot1[1]+d] == 0 and board[robot2[0]][robot2[1]+d] == 0:
                moves.append(((robot1[0], robot1[1]+d), robot1))
                moves.append(((robot2[0], robot2[1]+d), robot2))

    return moves


def solution(board):
    answer = 0
    que = deque([[((1, 1), (1, 2)), 0]])
    visited = set([((1, 1), (1, 2))])
    cost = 0
    n = len(board)
    new_board = [[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1] = board[i][j]
    while que:
        robot, cost = que.popleft()
        if (n, n) in robot:
            answer = cost
            break

        for next_move in can_moves(robot, new_board):
            if next_move not in visited:
                que.append((next_move, cost+1))
                visited.add(next_move)
    return answer


test1 = [[0, 0, 0, 1, 1], [0, 0, 0, 1, 0], [
    0, 1, 0, 1, 1], [1, 1, 0, 0, 1], [0, 0, 0, 0, 0]]

testcase = [test1]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
