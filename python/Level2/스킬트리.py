# https://programmers.co.kr/learn/courses/30/lessons/49993

def check_skill(skill, skill_tree):
    idx1 = 0
    idx2 = 0
    while idx1 < len(skill) and idx2 < len(skill_tree):
        if skill[idx1] == skill_tree[idx2]:
            idx1 += 1
        else:
            if skill_tree[idx2] in skill:
                return 0
        idx2 += 1
    else:
        return 1


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        answer += check_skill(skill, skill_tree)
    return answer
