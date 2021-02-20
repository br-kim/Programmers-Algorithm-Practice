# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq


def insert_data(min_heap, max_heap, data_dict, data):
    heapq.heappush(min_heap, data)
    heapq.heappush(max_heap, (-data, data))
    if data_dict.get(data):
        data_dict[data] += 1
    else:
        data_dict[data] = 1


def delete_data(min_heap, max_heap, data_dict, oper):
    deleted_data = None
    if oper == 1:
        while sum(data_dict.values()):
            deleted_data = heapq.heappop(max_heap)
            if data_dict.get(deleted_data[1]) > 0:
                data_dict[deleted_data[1]] -= 1
                break
            else:
                pass

    elif oper == -1:
        while sum(data_dict.values()):
            deleted_data = heapq.heappop(min_heap)
            if data_dict.get(deleted_data) > 0:
                data_dict[deleted_data] -= 1
                break
            else:
                pass


def solution(operations):
    min_heap = []
    max_heap = []
    data_dict = dict()
    for op in operations:
        op = op.split(" ")
        if op[0] == "I":
            insert_data(min_heap, max_heap, data_dict, int(op[1]))
        elif op[0] == "D":
            delete_data(min_heap, max_heap, data_dict, int(op[1]))
    value = [i for i in data_dict.keys() if data_dict[i] != 0]
    if not value:
        return [0, 0]
    else:
        return [max(value), min(value)]
