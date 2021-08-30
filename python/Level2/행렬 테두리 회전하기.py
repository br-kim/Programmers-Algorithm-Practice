# https://programmers.co.kr/learn/courses/30/lessons/77485


def solution(rows, columns, queries):
    answer = []
    board_line = [i for i in range(1, rows*columns+1)]
    board = []
    for _ in range(rows):
        buffer = []
        for _ in range(columns):
            buffer.append(board_line[0])
            board_line.pop(0)
        board.append(buffer)

    for query in queries:
        y1, x1, y2, x2 = [i-1 for i in query]
        min_values = []
        buffer = board[y1][x1]
        min_values.append(board[y1][x1])

        for y in range(y1, y2):
            board[y][x1] = board[y+1][x1]
            min_values.append(board[y][x1])

        for x in range(x1, x2):
            board[y2][x] = board[y2][x+1]
            min_values.append(board[y2][x])

        for y in range(y2, y1, -1):
            board[y][x2] = board[y-1][x2]
            min_values.append(board[y][x2])

        for x in range(x2, x1, -1):
            board[y1][x] = board[y1][x-1]
            min_values.append(board[y1][x])

        board[y1][x1+1] = buffer
        answer.append(min(min_values))

    return answer


test1 = 6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]
test2 = 3, 3, [[1, 1, 2, 2], [1, 2, 2, 3], [2, 1, 3, 2], [2, 2, 3, 3]]
test3 = 100, 97, [[1, 1, 100, 97]]
testcase = [test1, test2, test3]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
