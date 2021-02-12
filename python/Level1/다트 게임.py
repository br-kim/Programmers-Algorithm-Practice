# https://programmers.co.kr/learn/courses/30/lessons/17682

def check_sdt(s, score):
    if s == 'S':
        return score
    elif s == 'D':
        return score**2
    elif s == 'T':
        return score**3


def check_option(dartResult, score, before_score, idx):
    score, before_score = cal_option(dartResult[idx+1], score, before_score)
    idx += 1
    return score, before_score, idx


def cal_option(s, score, before_score):
    if s == "*":
        score = score*2
        before_score = before_score*2
    elif s == "#":
        score = score*-1
    return score, before_score


def solution(dartResult):
    answer = 0
    idx = 0
    before_score = 0

    while idx < len(dartResult):
        score = 0
        if dartResult[idx:idx+2].isdigit():
            idx += 2
            score = 10
            score = check_sdt(dartResult[idx], score)
            if idx < len(dartResult)-1 and dartResult[idx+1] in "*#":
                score, before_score, idx = check_option(
                    dartResult, score, before_score, idx)

        elif dartResult[idx].isdigit():
            score = int(dartResult[idx])
            idx += 1
            score = check_sdt(dartResult[idx], score)
            if idx < len(dartResult)-1 and dartResult[idx+1] in "*#":
                score, before_score, idx = check_option(
                    dartResult, score, before_score, idx)

        answer += before_score
        before_score = score
        idx += 1

    return answer+score
