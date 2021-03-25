# https://programmers.co.kr/learn/courses/30/lessons/60062

from itertools import permutations


def make_weaks(n, weak):
    weaks = [weak]
    w = []
    for i in range(1, len(weak)):
        w = weak[:]
        for idx in range(i):
            w[idx] += n
        weaks.append(sorted(w))
    return weaks


def solution(n, weak, dist):
    # 취약 지점을 일렬로 펼침.
    weaks = make_weaks(n, weak)
    for num_friends in range(1, len(dist) + 1):
        for weak in weaks:
            dists = [list(i) for i in permutations(dist, num_friends)]
            for d in dists:
                idx = 0
                while d:
                    remain = d.pop()
                    while True:
                        if idx < len(weak) - 1:
                            distance = weak[idx + 1] - weak[idx]
                        else:
                            return num_friends
                        idx += 1
                        if remain > distance:
                            remain = remain - distance
                        else:
                            break

    return -1


test1 = 12, [1, 5, 6, 10], [1, 2, 3, 4]
test2 = 12, [1, 3, 4, 9, 10], [3, 5, 7]
test3 = 200, [0, 10, 50, 80, 120, 160], [1, 10, 5, 40, 30]
test4 = 200, [0, 100], [1, 1]
testcase = [test1, test2, test3, test4]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1], test[2]))
