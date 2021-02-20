# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    gen_dict = dict()
    gens = []
    gen_dict2 = dict()
    for idx, i in enumerate(zip(genres, plays)):
        genre = i[0]
        play = i[1]
        if gen_dict2.get(genre):
            gen_dict2[genre].append([idx, play])
        else:
            gen_dict2[genre] = [[idx, play]]
        if genre not in gens:
            gens.append(genre)
        if gen_dict.get(genre):
            gen_dict[genre] += play
        else:
            gen_dict[genre] = play
    gens.sort(key=lambda x: -gen_dict[x])
    for gen in gens:
        for i in range(len(gen_dict2[gen])):
            if i == 2:
                break
            f = sorted(gen_dict2[gen], key=lambda x: (-x[1], x[0]))
            answer.append(f[i][0])
    return answer
