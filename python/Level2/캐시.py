# https://programmers.co.kr/learn/courses/30/lessons/17680

from collections import deque


def solution(cacheSize, cities):
    cache = deque()
    answer = 0
    cities = [c.lower() for c in cities]
    if cacheSize == 0:
        return len(cities)*5

    for city in cities:
        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()
            cache.append(city)
            answer += 5
        elif city in cache:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer
