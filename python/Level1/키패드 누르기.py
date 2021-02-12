# https://programmers.co.kr/learn/courses/30/lessons/67256

keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]


def cal_dist(num, xy):
    # 1.1 2.2 3.1 4.1 5.3 62 73 84 93 104
    arr = [0, 1, 2, 1, 2, 3, 2, 3, 4, 3, 4]
    diff = abs(num-int(keypad[xy[0]][xy[1]]))
    return arr[diff]


def cal_xy(num):
    for idx_x, x in enumerate(keypad):
        for idx_y, y in enumerate(x):
            if num == y:
                return [idx_x, idx_y]


def move_hand(number, left_hand, right_hand, hand):
    if number in [1, 4, 7]:
        left_hand = cal_xy(number)
        return 'L', left_hand, right_hand
    elif number in [3, 6, 9]:
        right_hand = cal_xy(number)
        return 'R', left_hand, right_hand
    else:
        if cal_dist(number, left_hand) == cal_dist(number, right_hand):
            if hand == 'left':
                left_hand = cal_xy(number)
                return 'L', left_hand, right_hand
            else:
                right_hand = cal_xy(number)
                return 'R', left_hand, right_hand
        elif cal_dist(number, left_hand) < cal_dist(number, right_hand):
            left_hand = cal_xy(number)
            return 'L', left_hand, right_hand
        else:
            right_hand = cal_xy(number)
            return 'R', left_hand, right_hand


def solution(numbers, hand):
    answer = ''
    left_hand, right_hand = [3, 0], [3, 2]
    for number in numbers:
        if number == 0:
            number = 11
        ans, left_hand, right_hand = move_hand(
            number, left_hand, right_hand, hand)
        answer += ans
    return answer
