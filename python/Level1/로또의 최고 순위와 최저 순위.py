# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    answer = []
    matched = 0
    unknown = 0
    for i in lottos:
        if i in win_nums:
            matched += 1
        if i == 0:
            unknown += 1
    rank = [6, 6, 5, 4, 3, 2, 1]
    high = rank[matched+unknown]
    low = rank[matched]
    return [high, low]


test1 = [44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]
test2 = [0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]
test3 = [45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]
testcase = [test1, test2, test3]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
