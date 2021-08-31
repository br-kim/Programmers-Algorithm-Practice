# https://programmers.co.kr/learn/courses/30/lessons/77885


def solution(numbers):
    answer = []
    for number in numbers:
        end = bin(number)[-2:]
        if end == '11':
            a = bin(number).replace(
                '0b', '0')
            a = a[::-1]
            a = a.replace('10', '01', 1)
            a = a[::-1]
            answer.append(int(a, 2))
        else:
            answer.append(number+1)

    return answer
    # return [int(bin(n).replace(
    #             '0b', '0')[::-1].replace('10', '01', 1)[::-1], 2) if bin(n)[-2:] == '11' else n+1 for n in numbers]


test1 = [2, 7]

testcase = [test1]


for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    if isinstance(test, tuple):
        print("실행 결과:", solution(*test))
    else:
        print("실행 결과:", solution(test))
