# https://programmers.co.kr/learn/courses/30/lessons/12950

def solution(arr1, arr2):
    res = []
    print(arr1[0])
    for j in range(len(arr1)):
        ans = []
        for i in range(len(arr1[0])):
            ans.append(arr1[j][i] + arr2[j][i])
        res.append(ans)
    return res
