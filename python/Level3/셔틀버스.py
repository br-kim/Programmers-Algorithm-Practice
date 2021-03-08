# https://programmers.co.kr/learn/courses/30/lessons/17678

def time_to_minute(time):
    h, m = [int(i) for i in time.split(":")]
    return h*60 + m


def minute_to_time(minute):
    h, m = str(minute // 60).zfill(2), str(minute % 60).zfill(2)
    return h+":"+m


def solution(n, t, m, timetable):
    timetable.sort()
    bus_arrive_time = ["09:00"]
    bus_dict = dict()
    answer = ''
    for _ in range(n-1):
        next_arrive = time_to_minute(bus_arrive_time[-1]) + t
        bus_arrive_time.append(minute_to_time(next_arrive))

    for i in bus_arrive_time:
        bus_dict[i] = []

    idx = 0
    for bus_time in bus_arrive_time:
        while idx < len(timetable):
            if len(bus_dict[bus_time]) == m:
                break
            if timetable[idx] <= bus_time:
                bus_dict[bus_time].append(timetable[idx])
                idx += 1
            else:
                break

    last_time = bus_arrive_time[-1]

    if len(bus_dict[last_time]) < m:
        # 버스가 꽉 차지 않았다.
        answer = last_time
    else:
        # 버스가 꽉 찼다.
        last = bus_dict[last_time][-1]
        answer = minute_to_time(time_to_minute(last) - 1)

    return answer


test1 = 1, 1, 5, ["08:00", "08:01", "08:02", "08:03"]
test2 = 2, 10, 2, ["09:10", "09:09", "08:00"]
test3 = 2, 1, 2, ["09:00", "09:00", "09:00", "09:00"]
test4 = 1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"]
test5 = 1, 1, 1, ["23:59"]
test6 = 10, 60, 45, ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
                     "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
testcase = [test1, test2, test3, test4, test5, test6]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test[0], test[1], test[2], test[3]))
