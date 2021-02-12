# https://programmers.co.kr/learn/courses/30/lessons/64061

def return_first(board):
    for idx, val in enumerate(board):
        if val != 0:
            board[idx] = 0
            return val, board
    else:
        return 0, board


def solution(board, moves):
    goal = []
    my_board = list(zip(*board))
    counter = 0
    for move in moves:
        for idx, one_board in enumerate(my_board):
            if idx+1 == move:
                val, new_board = return_first(list(one_board))
                if val == 0:
                    continue
                my_board[idx] = new_board
                goal.append(val)
                if len(goal) >= 2:
                    if goal[-1] == goal[-2]:
                        goal.pop()
                        goal.pop()
                        counter += 2
    return counter
