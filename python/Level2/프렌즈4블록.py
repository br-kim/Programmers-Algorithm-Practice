# https://programmers.co.kr/learn/courses/30/lessons/17679

def init_board(board):
    new_board = [['0']*(len(board[0])+1)]
    for i in board:
        buf = ['0']
        buf.extend(i)
        new_board.append(buf)
    return new_board


def board_check(board):
    flag = False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][-1] != '0':
                n = board[i][j]
                left = board[i][j-1]
                up = board[i-1][j]
                left_up = board[i-1][j-1]
                if n[-1] == up[-1] == left_up[-1] == left[-1]:
                    board[i][j] = "2"+n[-1]
                    board[i][j-1] = "2"+n[-1]
                    board[i-1][j] = "2"+n[-1]
                    board[i-1][j-1] = "2"+n[-1]
                    flag = True
    return board, flag


def board_clear(board):
    cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j][0] == '2':
                board[i][j] = '0'
                cnt += 1
    return board, cnt


def board_down(board):
    for i in range(len(board)-1, -1, -1):
        for j in range(len(board[0])):
            if board[i][j] == '0':
                idx = -1
                while i+idx > -1:
                    if board[i+idx][j] != '0':
                        board[i][j] = board[i+idx][j]
                        board[i+idx][j] = '0'
                        break
                    else:
                        idx -= 1
    return board


def solution(m, n, board):
    answer = 0
    new_board = init_board(board)  # 왼쪽, 위 줄에 0 추가
    while True:
        new_board, flag = board_check(new_board)
        if not flag:
            break
        new_board, deleted = board_clear(new_board)
        answer += deleted
        new_board = board_down(new_board)
    return answer
