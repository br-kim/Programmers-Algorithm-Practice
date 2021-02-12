# https://programmers.co.kr/learn/courses/30/lessons/12906

def solution(arr):
    ans = [arr[0]]
    idx = 1
    while True:
        if idx == len(arr):
            break
        if arr[idx-1] == arr[idx]:
            pass
        else:
            ans.append(arr[idx])
        idx += 1
    return ans
