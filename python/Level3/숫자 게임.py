# https://programmers.co.kr/learn/courses/30/lessons/12987

def solution(A, B):
    answer = 0
    idx1 = 0
    idx2 = 0
    A.sort()
    B.sort()
    while idx2 < len(A):
        if A[idx1] < B[idx2]:
            answer += 1
            idx1 += 1
            idx2 += 1
        else:
            idx2 += 1

    return answer


test1 = [5, 1, 3, 7], [2, 2, 6, 8]
test2 = [2, 2, 2, 2], [1, 1, 1, 1]
testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
