# https://programmers.co.kr/learn/courses/30/lessons/17686

def solution(files):
    arr = []
    for file in files:
        head, number = "", ""
        flag = True
        for f in file:
            if f.isdigit():
                number += f
                flag = False
            elif flag:
                head += f
            else:
                break
        arr.append([file, head, number])
        arr.sort(key=lambda x: (x[1].lower(), int(x[2])))
    return [i[0] for i in arr]
