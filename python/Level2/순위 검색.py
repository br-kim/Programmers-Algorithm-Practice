# https://programmers.co.kr/learn/courses/30/lessons/72412

from itertools import combinations


def makeInfoDictionary(info):
    dic = dict()
    for i in info:
        t = i.split()
        _info = t[:-1]
        score = int(t[-1])
        for n in range(5):
            comb = list(combinations(range(4), n))
            for c in comb:
                c_info = _info.copy()
                for v in c:
                    c_info[v] = '-'
                changed_comb = '/'.join(c_info)
                if changed_comb in dic:
                    dic[changed_comb].append(score)
                else:
                    dic[changed_comb] = [score]
    for val in dic.values():
        val.sort()

    return dic


def lowerBound(data, query_score):
    begin, end = 0, len(data)
    while begin != end and begin != len(data):
        if data[(begin + end) // 2] >= query_score:
            end = (begin + end) // 2
        else:
            begin = (begin + end) // 2 + 1
    return begin


def solution(info, query):
    answer = []
    db = makeInfoDictionary(info)
    for q in query:
        _query = [i for i in q.split() if i != 'and']
        _query_cnd = '/'.join(_query[:-1])
        _query_score = int(_query[-1])
        if _query_cnd in db:
            data = db[_query_cnd]
            if len(data) > 0:
                higher_scored = len(data) - lowerBound(data, _query_score)
                answer.append(higher_scored)
        else:
            answer.append(0)
    return answer


test1 = ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150", "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"], [
    "java and backend and junior and pizza 100", "python and frontend and senior and chicken 200", "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100", "- and - and - and - 150"]


testcase = [test1]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
