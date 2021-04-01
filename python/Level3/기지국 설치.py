# https://programmers.co.kr/learn/courses/30/lessons/12979

def solution(n, stations, w):
    idx = 0
    begin = 0
    end = len(stations) - 1
    sections = []
    answer = 0
    while True:
        if idx == begin:
            sections.append(stations[idx]-w-1)
        else:
            sections.append((stations[idx]-w) - (stations[idx-1]+w)-1)
        if idx == end:
            sections.append(n-(stations[idx]+w))
            break
        idx += 1
    coverage = (1 + (2 * w))
    for s in sections:
        if s > 0:
            if s % coverage:
                answer += (s // coverage) + 1
            else:
                answer += s // coverage
    return answer


test1 = 11, [4, 11], 1
test2 = 16, [9], 2


testcase = [test1, test2, ]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(*test))
