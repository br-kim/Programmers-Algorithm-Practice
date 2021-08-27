# https://programmers.co.kr/learn/courses/30/lessons/84325

def solution(table, languages, preference):
    langprefer = dict(zip(languages, preference))
    occ_score = dict()
    for t in table:
        occupation, *score = t.split()
        total = 0
        for i, s in enumerate(score):
            if s in languages:
                total += langprefer[s]*(5-i)
        occ_score[occupation] = total
    return min(occ_score, key=lambda x: (-occ_score[x], x))


test1 = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]
test2 = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT",
         "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]
testcase = [test1, test2]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
