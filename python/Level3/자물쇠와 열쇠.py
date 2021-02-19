# https://programmers.co.kr/learn/courses/30/lessons/60059

def rotateLeft90D(board):
    return list(zip(*[reversed(i) for i in board]))


def extendBoard(n, board):
    newline = [1] * (2 * (n - 1)) + [1] * len(board)
    newboard = []
    for _ in range(n-1):
        newboard.append(newline[:])
    for b in board:
        newboard.append([1] * (n-1) + b + [1] * (n-1))
    for _ in range(n-1):
        newboard.append(newline[:])
    return newboard


def isCanOpen(key, lock, x, y, hole):
    len_key = len(key)
    filled = 0
    begin_lock = len_key - 1
    end_lock = len(lock)-(len_key-1)
    for i in range(len_key):
        for j in range(len_key):
            if not (begin_lock <= i + y < end_lock) or not (begin_lock <= j + x < end_lock):
                continue
            if key[i][j] == lock[i + y][j + x]:
                return False
            if key[i][j] == 1 and lock[i + y][j + x] == 0:
                filled += 1
    if hole == filled:
        return True
    else:
        return False


def solution(key, lock):
    lockhole = 0
    for i in lock:
        lockhole += i.count(0)
    extendLock = extendBoard(len(key), lock)

    for _ in range(4):
        for i in range(len(lock)+len(key)-1):
            for j in range(len(lock)+len(key)-1):
                if isCanOpen(key, extendLock, j, i, lockhole):
                    return True
        key = rotateLeft90D(key)
    return False


test1 = [[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
