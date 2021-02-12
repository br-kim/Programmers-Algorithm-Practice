# https://programmers.co.kr/learn/courses/30/lessons/68936

def divide(arr):
    global zeroone
    if len(arr) == 2:
        for i in arr:
            for j in i:
                zeroone[j] += 1
        return
    lis = [0, len(arr)//2], [0, 0], [len(arr)//2,
                                     0], [len(arr)//2, len(arr)//2]
    for elem in lis:
        y, x = elem
        val = arr[y][x]
        esc = False
        new_arr1 = []
        for i in range(y, y+len(arr)//2):
            new_arr2 = []
            for j in range(x, x+len(arr)//2):
                new_arr2.append(arr[i][j])
                if val != arr[i][j]:
                    esc = True
            new_arr1.append(new_arr2)
        if esc:
            divide(new_arr1)
        else:
            zeroone[val] += 1
    return


def solution(arr):
    sumvalue = sum([sum(i) for i in arr])
    if sumvalue == 0:
        return [1, 0]
    elif sumvalue == len(arr)**2:
        return [0, 1]
    global zeroone
    zeroone = [0, 0]
    divide(arr)
    return zeroone
