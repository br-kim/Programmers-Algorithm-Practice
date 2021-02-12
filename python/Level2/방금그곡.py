# https://programmers.co.kr/learn/courses/30/lessons/17683

def make_full_music(length, music):
    full_music = []
    idx = 0
    while len(full_music) < length:
        full_music.append(music[idx])
        idx += 1
        if idx == len(music):
            idx = 0
    return full_music


def divide_music(music):
    arr = []
    for i in range(len(music)-1):
        if music[i].isalpha():
            if music[i+1] == '#':
                arr.append(music[i]+'#')
            else:
                arr.append(music[i])
    if music[-1].isalpha():
        arr.append(music[-1])
    return arr


def cal_time(time1, time2):
    mt1 = h_to_m(time1)
    mt2 = h_to_m(time2)
    return mt2 - mt1


def h_to_m(time1):
    h, m = [int(i) for i in time1.split(':')]
    mt = h * 60 + m
    return mt


def is_music(m, full_music):
    idx = 0
    while idx < len(full_music)-len(m)+1:
        idx1 = 0
        while idx1 < len(m):
            if m[idx1] == full_music[idx+idx1]:
                idx1 += 1
            else:
                break
        else:
            return True
        idx += 1
    return False


def solution(m, musicinfos):
    m = divide_music(m)
    ans = []
    for musicinfo in musicinfos:
        start, end, title, music = musicinfo.split(",")
        music = divide_music(music)
        play_time = cal_time(start, end)
        full_music = make_full_music(play_time, music)
        if is_music(m, full_music):
            ans.append([play_time, len(ans), title])
    if ans:
        ans.sort(key=lambda x: (-x[0], x[1]))
        return ans[0][2]
    else:
        return "(None)"
