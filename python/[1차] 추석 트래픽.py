# https://programmers.co.kr/learn/courses/30/lessons/17676

def timetosec(time):
    h, m, s = time.split(":")
    h = int(h) * 3600
    m = int(m) * 60
    total = h + m + float(s)
    return total


def sectosec(sec):
    return float(sec[:-1])


def isInRange1(ori, ran):
    ori_begin = ori[0]
    ori_end = ori[1]
    ran_begin = ran[0]
    ran_end = ran[1]

    if ran_end < ori_end:
        return False
    elif ran_begin >= ori_end + 1:
        return False
    else:
        return True


def solution(lines):
    arr = []
    ans = []
    for line in lines:
        end = timetosec(line.split()[1])
        begin = timetosec(line.split()[1]) - sectosec(line.split()[2])
        arr.append([round(round(begin, 3)+0.001, 3), end])
    for i in range(len(arr)):
        a = 0
        for ii in range(len(arr)):
            if isInRange1(arr[i], arr[ii]):
                a += 1
        ans.append(a)
    return max(ans)


test1 = ["2016-09-15 00:00:00.000 3s"]
test2 = ["2016-09-15 23:59:59.999 0.001s"]
test3 = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
test4 = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
test5 = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s",
         "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
test6 = ["2016-09-15 00:00:00.000 2.3s", "2016-09-15 23:59:59.999 0.1s"]
testcase = [test1, test2, test3, test4, test5, test6]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
