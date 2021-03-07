# https://programmers.co.kr/learn/courses/30/lessons/42892

import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)


class Node:
    def __init__(self, num, loc):
        self.num = num
        self.left = None
        self.right = None
        self.loc = loc
        self.x = loc[0]
        self.y = loc[1]


ans = []


def traversal1(node):
    global ans
    if node:
        ans.append(node.num)
        traversal1(node.left)
        traversal1(node.right)


def traversal2(node):
    global ans
    if node:
        traversal2(node.left)
        traversal2(node.right)
        ans.append(node.num)


def solution(nodeinfo):
    answer = []
    nodelist = []
    for idx, node in enumerate(nodeinfo):
        nodelist.append(Node(idx + 1, node))
    nodelist.sort(key=lambda x: [-x.loc[1], x.loc[0]])
    nextidx = 1
    top = nodelist[0]
    while nextidx < len(nodelist):
        nextt = nodelist[nextidx]
        if nextt.x < top.x:
            if not top.left:
                top.left = nextt
                nextidx += 1
            else:
                top = top.left
                continue
        else:
            if not top.right:
                top.right = nextt
                nextidx += 1
            else:
                top = top.right
                continue
        top = nodelist[0]
    global ans
    ans = []
    traversal1(nodelist[0])
    answer.append(ans)
    ans = []
    traversal2(nodelist[0])
    answer.append(ans)
    return answer


test1 = [[5, 3], [11, 5], [13, 3], [3, 5],
         [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
testcase = [test1]
for idx, test in enumerate(testcase):
    print("----------------")
    print(f"테스트 {idx+1}")
    print("출력 : ")
    print("실행 결과:", solution(test))
