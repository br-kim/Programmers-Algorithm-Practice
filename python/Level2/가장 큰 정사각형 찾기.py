# https://programmers.co.kr/learn/courses/30/lessons/12905

def solution(board):
    maxv = 0
    if len(board[0]) == 1 and len(board) == 1:
        return board[0][0]
    new_board = [[0]*(len(board[0])+1)]

    for i, v in enumerate(board):
        nb = [0]
        nb.extend(board[i])
        new_board.append(nb)
    board = new_board
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] >= 1):
                board[i][j] = min(board[i][j-1], board[i-1]
                                  [j-1], board[i-1][j]) + 1
                maxv = max(board[i][j], maxv)

    return maxv**2
