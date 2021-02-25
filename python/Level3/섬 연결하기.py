# https://programmers.co.kr/learn/courses/30/lessons/42861

parent = []
rank = []


def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if rank[x] > rank[y]:
        x, y = y, x
    parent[x] = y
    if rank[x] == rank[y]:
        rank[y] += 1
    return True


def solution(n, costs):
    global parent, rank
    parent = [i for i in range(n)]
    rank = [0]*n
    costs.sort(key=lambda x: x[2])
    answer = 0
    for i in costs:
        if union(i[0], i[1]):
            answer += i[2]
    return answer


test1 = 4, [[0, 1, 1], [0, 2, 2], [1, 2, 5], [1, 3, 1], [2, 3, 8]]
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1]))
