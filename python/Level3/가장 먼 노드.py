# https://programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque


def bfs(start, check, a, dist):
    q = deque()
    q.append(start)
    check[start] = True
    while q:
        x = q.popleft()
        for i in range(len(a[x])):
            y = a[x][i]
            if not check[y]:
                dist[y] = dist[x]+1
                q.append(y)
                check[y] = True
    return dist


def solution(n, edge):
    check = [False for i in range(n+1)]
    adj = [[]for i in range(n+1)]
    dist = [0 for i in range(n+1)]
    for i in edge:
        if i[1] not in adj[i[0]]:
            adj[i[0]].append(i[1])
        if i[0] not in adj[i[1]]:
            adj[i[1]].append(i[0])

    dist = bfs(1, check, adj, dist)

    return dist.count(max(dist))
