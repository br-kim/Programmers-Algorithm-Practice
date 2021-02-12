# https://programmers.co.kr/learn/courses/30/lessons/17684

def solution(msg):
    alpha = [chr(i) for i in range(65, 91)]
    dic = dict()
    ans = []
    for i in range(1, 27):
        dic[alpha[i-1]] = i
    left = 0
    while left < len(msg):
        right = left+1
        while True:
            if dic.get(msg[left:right]) and right < len(msg):
                right += 1
            elif not dic.get(msg[left:right]):
                dic[msg[left:right]] = len(dic)+1
                right -= 1
                ans.append(dic[msg[left:right]])
                break
            else:
                ans.append(dic[msg[left:right]])
                break

        left += len(msg[left:right])
    return ans
