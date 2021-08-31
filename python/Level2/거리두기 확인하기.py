# https://programmers.co.kr/learn/courses/30/lessons/81302

def check_board(board):
    for y in range(len(board)):
        for x in range(len(board[0])):
            if board[y][x] == "P":
                # 가로 세로의 경우
                if y < len(board)-1 and board[y+1][x] == "P":
                    return False
                if y > 0 and board[y-1][x] == "P":
                    return False
                if x < len(board[0])-1 and board[y][x+1] == "P":
                    return False
                if x > 0 and board[y][x-1] == "P":
                    return False

                if y < len(board)-2 and board[y+2][x] == "P":
                    if board[y+1][x] != "X":
                        return False
                if y > 1 and board[y-2][x] == "P":
                    if board[y-1][x] != "X":
                        return False
                if x < len(board[0])-2 and board[y][x+2] == "P":
                    if board[y][x+1] != "X":
                        return False
                if x > 1 and board[y][x-2] == "P":
                    if board[y][x-1] != "X":
                        return False

                # 대각선의 경우
                if y < len(board)-1 and x < len(board[0])-1 and board[y+1][x+1] == "P":
                    if board[y+1][x] == "X" and board[y][x+1] == "X":
                        pass
                    else:
                        return False
                if y > 0 and x < len(board[0])-1 and board[y-1][x+1] == "P":
                    if board[y-1][x] == "X" and board[y][x+1] == "X":
                        pass
                    else:
                        return False
                    pass
                if y < len(board)-1 and x > 0 and board[y+1][x-1] == "P":
                    if board[y+1][x] == "X" and board[y][x-1] == "X":
                        pass
                    else:
                        return False
                    pass
                if y > 0 and x > 0 and board[y-1][x-1] == "P":
                    if board[y-1][x] == "X" and board[y][x-1] == "X":
                        pass
                    else:
                        return False
                    pass

    return True


def solution(places):
    answer = []
    for p in places:
        if check_board(p):
            answer.append(1)
        else:
            answer.append(0)

    return answer


test1 = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
]


testcase = [test1]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
