# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)):
        ans = 0
        for j in range(i+1, len(prices)):
            ans += 1
            if prices[i] <= prices[j]:
                pass
            else:
                break
        answer.append(ans)
    return answer
