# https://programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    path = set()
    direction = {
        "U": [1, 0],
        "L": [0, -1],
        "R": [0, 1],
        "D": [-1, 0]
    }
    pos = [0, 0]
    for d in dirs:
        if abs(pos[0] + direction[d][0]) > 5 or abs(pos[1] + direction[d][1]) > 5:
            continue
        beforepos = tuple(pos[:])
        pos[0] += direction[d][0]
        pos[1] += direction[d][1]
        route = tuple(sorted((beforepos, tuple(pos))))
        path.add(route)
    return len(path)


test1 = "ULURRDLLU"
test2 = "LULLLLLLU"
testcase = [test1, test2]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
