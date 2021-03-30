# https://programmers.co.kr/learn/courses/30/lessons/67258

from collections import defaultdict


def solution(gems):
    begin = 0
    end = 0
    all_kind_length = len(set(gems))
    now_dict = defaultdict(int)
    ans_list = []
    # begin도 끝까지 확인 필요
    while begin < len(gems):
        now_size = len(now_dict.keys())
        if now_size < all_kind_length and end < len(gems):
            now_dict[gems[end]] += 1
            end += 1
        else:
            while all_kind_length <= len(now_dict.keys()) and begin < end:
                now_size = len(now_dict.keys())
                now_dict[gems[begin]] -= 1
                if now_dict[gems[begin]] == 0:
                    now_dict.pop(gems[begin])
                if now_size == all_kind_length:
                    ans_list.append([begin + 1, end])
                begin += 1
            else:
                now_dict[gems[begin]] -= 1
                if now_dict[gems[begin]] == 0:
                    now_dict.pop(gems[begin])
                begin += 1

    return sorted(ans_list, key=lambda x: (x[1]-x[0], x[0]))[0]


test1 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
test2 = ["AA", "AB", "AC", "AA", "AC"]
test3 = ["XYZ", "XYZ", "XYZ"]
test4 = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]
test5 = ["A", "A", "B"]
test6 = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD",
         "SAPPHIRE", "DIA", "RUBY", "EMERALD", "SAPPHIRE"]
testcase = [test1, test2, test3, test4, test5, test6]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
