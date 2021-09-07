# https://programmers.co.kr/learn/courses/30/lessons/12952


def solution(n):
    answer = 0
    count = 0
    arr = [0]*n

    def nQueen(depth):
        nonlocal count
        if depth == n:
            count += 1
            return
        for i in range(n):
            arr[depth] = i
            if isPossible(depth):
                nQueen(depth+1)

    def isPossible(col):
        for i in range(col):
            if arr[col] == arr[i]:
                return False
            elif abs(col-i) == abs(arr[col]-arr[i]):
                return False
        return True

    nQueen(0)
    return count


test1 = 5

testcase = [test1]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
