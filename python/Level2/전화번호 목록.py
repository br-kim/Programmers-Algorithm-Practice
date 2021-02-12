# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone):
    answer = True
    idx = 0
    phone_asc = sorted(phone, key=lambda x: len(x))
    phone_dec = sorted(phone, key=lambda x: len(x), reverse=True)
    for idx in range(len(phone)):
        for i in range(idx, len(phone)):
            phone_idx_len = len(phone_asc[idx])
            if phone_idx_len > len(phone_dec[i]):
                break
            if phone_asc[idx] == phone_dec[i][:phone_idx_len] and phone_asc[idx] != phone_dec[i]:
                return False
    return answer
