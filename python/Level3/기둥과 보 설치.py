# https://programmers.co.kr/learn/courses/30/lessons/60061

# 기둥 0
# 보 1

def is_can_pillar(x, y, board):
    # 기둥이 설치될 수 있으려면
    # 바닥에 있거나
    if y == 0:
        return True
    # 보의 한쪽 끝 부분 위에 있거나 (x-1, x)
    if (x > 0 and 1 in board[y][x - 1]) or 1 in board[y][x]:
        return True
    # 다른 기둥 위에 있어야 한다.
    if y > 0 and 0 in board[y-1][x]:
        return True

    return False


def is_can_beam(x, y, board):
    # 보가 설치될 수 있으려면
    # 한쪽 끝 부분이 기둥 위에 있거나 (x or x+1)
    if (y > 0 and 0 in board[y - 1][x]) or (y > 0 and x < len(board)-1 and 0 in board[y - 1][x + 1]):
        return True
    # 양쪽 끝 부분이 다른 보와 동시에 연뎔되어 있어야 한다. (x-1 and x+1)
    if (x > 0 and 1 in board[y][x - 1]) and (x < len(board)-1 and 1 in board[y][x + 1]):
        return True

    return False


def solution(n, build_frame):
    board = [[[] for _ in range(n+1)] for _ in range(n+1)]

    for build in build_frame:
        x, y, kind, comm = build
        if comm == 1:  # 설치
            # 설치가 가능한 지 확인하고 설치해야 한다.
            if kind == 0:  # 기둥 설치
                if is_can_pillar(x, y, board):
                    board[y][x].append(0)

            if kind == 1:  # 보 설치
                if is_can_beam(x, y, board):
                    board[y][x].append(1)

        elif comm == 0:  # 삭제
            ori = board[y][x][:]
            if kind == 0:
                board[y][x].remove(0)

            elif kind == 1:
                board[y][x].remove(1)

            # 일부만 검사
            if kind == 0:  # 기둥 삭제
                # 기둥이 삭제되어도 내 윗 기둥(y+1)이 설치 가능한지?
                if y < len(board) - 1 and 0 in board[y + 1][x]:
                    if not is_can_pillar(x, y + 1, board):
                        board[y][x] = ori[:]
                        continue
            # 기둥이 삭제되어도 내 윗 보들(x, x-1)이 설치 가능한지?
                if y < len(board) - 1 and 1 in board[y + 1][x]:
                    if not is_can_beam(x, y + 1, board):
                        board[y][x] = ori[:]
                        continue
                if y < len(board) - 1 and x > 0 and 1 in board[y + 1][x - 1]:
                    if not is_can_beam(x-1, y + 1, board):
                        board[y][x] = ori[:]
                        continue

            if kind == 1:  # 보 삭제
                # 보가 삭제되어도 내 양 옆의 보(x-1,x+1)가 설치 가능한지?
                if x > 0 and 1 in board[y][x-1]:
                    if not is_can_beam(x-1, y, board):
                        board[y][x] = ori[:]
                        continue
                if x < len(board)-1 and 1 in board[y][x + 1]:
                    if not is_can_beam(x+1, y, board):
                        board[y][x] = ori[:]
                        continue

                # 보가 삭제되어도 내 양 옆의 기둥(x, x+1)이 설치 가능한지?
                if 0 in board[y][x]:
                    if not is_can_pillar(x, y, board):
                        board[y][x] = ori[:]
                        continue
                if x < len(board)-1 and 0 in board[y][x + 1]:
                    if not is_can_pillar(x + 1, y, board):
                        board[y][x] = ori[:]
                        continue

            # 전체검사
            # ori_x, ori_y = x, y
            # flag = True
            # for y in range(len(board)):
            #     for x in range(len(board)):
            #         for installed in board[y][x]:
            #             if installed == 0:
            #                 if not is_can_pillar(x, y, board):
            #                     board[ori_y][ori_x] = ori[:]
            #                     flag = False
            #                     break
            #             if installed == 1:
            #                 if not is_can_beam(x, y, board):
            #                     board[ori_y][ori_x] = ori[:]
            #                     flag = False
            #                     break
            #     if not flag:
            #         break
    answer = []
    for y in range(len(board)):
        for x in range(len(board)):
            if board[y][x]:
                for i in board[y][x]:
                    answer.append([x, y, i])
    answer.sort(key=lambda x: (x[0], x[1], x[2]))
    return answer


test1 = 5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [2, 2, 1, 1],
            [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]
test2 = 5, [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [
    2, 1, 1, 1], [3, 1, 1, 1], [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]

testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
