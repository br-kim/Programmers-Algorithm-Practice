# https://programmers.co.kr/learn/courses/30/lessons/64062

def check_stones(stones, mid, k):
    cnt = 0
    for s in stones:
        if s - mid < 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return True
    return False


def solution(stones, k):
    lo = 0
    hi = max(stones)
    while hi-1 > lo:
        mid = (hi + lo) // 2
        if check_stones(stones, mid, k):
            hi = mid
        else:
            lo = mid
    return hi


test1 = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
