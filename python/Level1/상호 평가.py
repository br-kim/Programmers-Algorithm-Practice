# https://programmers.co.kr/learn/courses/30/lessons/83201


def solution(scores):
    answer = ""
    for idx, value in enumerate(zip(*scores)):
        result = sum(value)
        len_value = len(value)
        if value[idx] in (min(value), max(value)):
            if value.count(value[idx]) == 1:
                result -= value[idx]
                len_value -= 1
        result = result / len_value
        if result >= 90:
            answer += "A"
        elif result >= 80:
            answer += "B"
        elif result >= 70:
            answer += "C"
        elif result >= 50:
            answer += "D"
        else:
            answer += "F"
    return answer


testcase = {
    "test1": [
        [100, 90, 98, 88, 65],
        [50, 45, 99, 85, 77],
        [47, 88, 95, 80, 67],
        [61, 57, 100, 80, 65],
        [24, 90, 94, 75, 65],
    ],
    "test2": [[50, 90], [50, 87]],
    "test3": [[70, 49, 90], [68, 50, 38], [73, 31, 100]],
}


for idx, test in enumerate(testcase.values()):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
