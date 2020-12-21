from collections import defaultdict
record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]


def solution(record):
    answer = []
    result = []

    enter_str = "{uid}님이 들어왔습니다."
    leaver_str = "{uid}님이 나갔습니다."

    uid_dict = defaultdict(str)
    for reco in record:
        reco_list = reco.split(" ")

        if reco_list[0] == "Enter":
            answer.append(enter_str.format(uid=reco_list[1]))
            uid_dict[reco_list[1]] = reco_list[2]
        elif reco_list[0] == "Leave":
            answer.append(leaver_str.format(uid=reco_list[1]))

        elif reco_list[0] == "Change":
            uid_dict[reco_list[1]] = reco_list[2]

    for ans in answer:
        ans_list = ans.split("님")
        result.append(uid_dict[ans_list[0]] + "님" + ans_list[1])

    return result

print(solution(record))