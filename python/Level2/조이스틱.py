# https://programmers.co.kr/learn/courses/30/lessons/42860

def cal_near(alpha):
    return min(ord(alpha) - 65, 91-ord(alpha))


def solution(name):
    answer = 0
    name = list(name)
    index = 0
    while True:
        right = 1
        left = 1
        if name[index] != 'A':
            updown = cal_near(name[index])
            answer += updown
            name[index] = 'A'
        if name == ["A"]*len(name):
            break
        for i in range(1, len(name)):
            if name[index+i] == "A":
                right += 1
            else:
                break
        for i in range(1, len(name)):
            if name[index-i] == "A":
                left += 1
            else:
                break
        if right > left:
            answer += left
            index -= left
        else:
            answer += right
            index += right
    return answer
