# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []
    people1 = [1, 2, 3, 4, 5]
    people2 = [2, 1, 2, 3, 2, 4, 2, 5]
    people3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ans = [0, 0, 0]
    for i in range(len(answers)):
        if answers[i] == people1[i % 5]:
            ans[0] += 1
        if answers[i] == people2[i % 8]:
            ans[1] += 1
        if answers[i] == people3[i % 10]:
            ans[2] += 1
    for i, score in enumerate(ans):
        if score == max(ans):
            answer.append(i+1)
    return answer
