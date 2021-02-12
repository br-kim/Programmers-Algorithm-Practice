# https://programmers.co.kr/learn/courses/30/lessons/60057

def solution(s):
    answer = set()
    for j in range(1, len(s)//2+1):
        begin = 0
        compressed = ""
        cnt = 1
        flag = False
        while begin < len(s):
            end = begin+j
            before = s[begin:end]
            after = s[begin+len(before):end+len(before)]
            if before == after:
                cnt += 1
                flag = True
            elif cnt > 1 and flag and before != after:
                compressed += str(cnt) + before
                cnt = 1
            else:
                compressed += before
            begin += len(before)
        answer.add(compressed)
    if not answer:
        return len(s)
    else:
        return len(min(answer, key=len))
