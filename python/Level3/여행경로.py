# https://programmers.co.kr/learn/courses/30/lessons/43164

ans = None


def dfs(airport, tickets, route, t_len):
    global ans
    if len(route) == t_len:
        answer = [i[0] for i in route]+[route[-1][1]]
        if not ans:
            ans = answer
        elif ans > answer:
            ans = answer
    route = list(route)
    for t in tickets:
        if t[0] == airport:
            route.append(t)
            new_tickets = tickets[:]
            new_tickets.remove(t)
            dfs(t[1], new_tickets, tuple(route), t_len)
            route.pop()


def solution(tickets):
    global ans
    dfs("ICN", tickets, [], len(tickets))
    return ans
