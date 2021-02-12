# https://programmers.co.kr/learn/courses/30/lessons/42890

from itertools import combinations


def make_keys(relation):
    column_len = len(relation[0])
    dict_key = list(range(column_len))
    keys = []
    for i in range(1, len(relation[0])+1):
        keys += list(combinations(dict_key, i))
    return keys


def is_unique(relations, key):
    new_dict = dict()
    for relation in relations:
        new_key = " ".join([relation[column_num] for column_num in key])
        if new_dict.get(new_key):  # 이미 딕셔너리에 등록되어 있다면 유일성을 만족하지 못한다.
            return False
        else:
            new_dict[new_key] = 1
    else:
        return True


def is_minimal(candidate_keys, key):
    # 최소성 검증. 기존 후보키를 완전히 포함하는 키라면 최소성 만족하지 못한다.
    for candidate_key in candidate_keys:
        cnt = 0
        for key_value in key:
            if key_value in candidate_key:
                cnt += 1
        if cnt == len(candidate_key):
            return False
    else:
        return True


def solution(relation):
    keys = make_keys(relation)  # 가능한 모든 키의 조합을 구한다.
    candidate_keys = set()
    for key in keys:
        if is_unique(relation, key) and is_minimal(candidate_keys, key):
            candidate_keys.add(key)

    return len(candidate_keys)
