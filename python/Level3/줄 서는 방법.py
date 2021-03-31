# https://programmers.co.kr/learn/courses/30/lessons/12936

def fact(n):
    arr = [1]*(n+1)
    for i in range(1, n+1):
        arr[i] = arr[i-1]*i
    return arr


def solution(n, k):
    ori = [i for i in range(1, n + 1)]
    fact_list = fact(n)
    result = []
    k = k-1
    while n > 0:
        val1 = k % fact_list[n - 1]
        val2 = k // fact_list[n - 1]
        n = n - 1
        k = val1
        result.append(val2)
    answer = []
    for r in result:
        answer.append(ori.pop(r))
    return answer


test1 = 3, 5
test2 = 5, 31


testcase = [test1, test2, ]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
