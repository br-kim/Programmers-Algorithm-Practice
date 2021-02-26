# https://programmers.co.kr/learn/courses/30/lessons/42884


def solution(routes):
    answer = 0
    routes.sort()

    pos = routes[0][1]
    routes = routes[1:]
    answer += 1

    for item in routes:
        if item[0] <= pos:
            pos = min(item[1], pos)
        else:
            pos = item[1]
            answer += 1
    return answer


test1 = [[-20, 15], [-14, -5], [-18, -13], [-5, -3]]
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
