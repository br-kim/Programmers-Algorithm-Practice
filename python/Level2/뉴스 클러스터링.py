# https://programmers.co.kr/learn/courses/30/lessons/17677

from collections import Counter


def make_substr(str1):
    arr1 = []
    for i in range(len(str1)-1):
        substr = str1[i:i+2]
        if substr.isalpha():
            arr1.append(str1[i:i+2].lower())
    return arr1


def solution(str1, str2):
    set1 = Counter(make_substr(str1))
    set2 = Counter(make_substr(str2))
    if not (set1 or set2):
        return 65536
    else:
        return int((sum((set1 & set2).values()) / sum((set1 | set2).values()))*65536)
