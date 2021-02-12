# https://programmers.co.kr/learn/courses/30/lessons/42888

def solution(records):
    answer = []
    coms = []
    user_dict = dict()
    for record in records:
        splited_record = record.split()
        if len(splited_record) == 3:
            com, user_id, user_nick = splited_record
            user_dict[user_id] = user_nick
        elif len(splited_record) == 2:
            com, user_id = splited_record
        if com != "Change":
            coms.append((com, user_id))

    for idx in range(len(coms)):
        msg = ""
        com, user_id = coms[idx]
        if com == "Enter":
            msg = user_dict[user_id]+"님이 들어왔습니다."
        elif com == "Leave":
            msg = user_dict[user_id]+"님이 나갔습니다."
        answer.append(msg)
    return answer
