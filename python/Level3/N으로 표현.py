# https://programmers.co.kr/learn/courses/30/lessons/42895

def solution(N, number):
    answer = 0
    s = [set() for _ in range(8)]
    for i, v in enumerate(s):
        v.add(int(str(N)*(i+1)))
    for i in range(8):
        for j in range(i):
            for op1 in s[j]:
                for op2 in s[i-j-1]:
                    s[i].add(op1+op2)
                    s[i].add(op1-op2)
                    s[i].add(op1*op2)
                    if op2 != 0:
                        s[i].add(op1//op2)
        if number in s[i]:
            answer = i+1
            break
    else:
        answer = -1
    return answer
