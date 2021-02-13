# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        temp = []
        for order in orders:
            comb = combinations(sorted(order), c)
            temp += comb
        count = Counter(temp)
        if len(count) != 0 and max(count.values()) != 1:
            answer += ["".join(i)
                       for i in count if count[i] == max(count.values())]

    return sorted(answer)


test1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
test2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
test3 = ["XYZ", "XWY", "WXA"], [2, 3, 4]
testcase = [test1, test2, test3]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
