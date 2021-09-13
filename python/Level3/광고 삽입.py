# https://programmers.co.kr/learn/courses/30/lessons/72414

def time_to_sec(times):
    hour, minute, seconds = [int(i) for i in times.split(":")]
    minute += hour*60
    seconds += minute*60
    return seconds


def solution(play_time, adv_time, logs):
    answer = ''
    print(0, time_to_sec(play_time))
    print(time_to_sec(adv_time))
    sec_adv_time = time_to_sec(adv_time)
    logs.sort()
    for log in logs:
        begin, end = log.split("-")
        sec_begin = time_to_sec(begin)
        sec_end = time_to_sec(end)
        print(time_to_sec(begin), time_to_sec(end))
        # print(sec_begin+sec_adv_time, sec_end+sec_adv_time)
        for log2 in logs:
            begin2, end2 = log2.split("-")

    return answer


test1 = "02:03:55", "00:14:15", ["01:20:15-01:45:14", "00:25:50-00:48:29",
                                 "00:40:31-01:00:00", "01:37:44-02:02:30", "01:30:59-01:53:29"]
test2 = "99:59:59", "25:00:00", [
    "69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
test3 = "50:00:00", "50:00:00", [
    "15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

testcase = [test1, test2, test3]

for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
