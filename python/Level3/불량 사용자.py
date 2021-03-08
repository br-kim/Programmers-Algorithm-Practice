# https://programmers.co.kr/learn/courses/30/lessons/64064

from itertools import product


def is_fit_id(ori_id, std_pattern):
    idx = 0
    if len(ori_id) != len(std_pattern):
        return False
    while idx < len(ori_id):
        if ori_id[idx] == std_pattern[idx] or std_pattern[idx] == "*":
            idx += 1
        else:
            return False
    return True


def solution(user_id, banned_id):
    banned_ids = []
    for pattern in banned_id:
        buffer = []
        for user in user_id:
            if is_fit_id(user, pattern):
                buffer.append(user)
        banned_ids.append(buffer)
    comb = product(*banned_ids)
    result = [frozenset(i)
              for i in comb if len(frozenset(i)) == len(banned_ids)]
    answer = len(set(result))
    return answer


test1 = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]
test2 = ["frodo", "fradi", "crodo", "abc123",
         "frodoc"], ["*rodo", "*rodo", "******"]
test3 = ["frodo", "fradi", "crodo", "abc123", "frodoc"], [
    "fr*d*", "*rodo", "******", "******"]
testcase = [test1, test2, test3]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
