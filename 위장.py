def solution(clothes):
    cloth_dict = {}
    for name, kind in clothes:
        if not kind in cloth_dict.keys():
            cloth_dict[kind] = [name]
        else:
            cloth_dict[kind].append(name)

    answer = 1

    for kind in cloth_dict.keys():
        num = len(cloth_dict[kind])

        answer = answer * (num+1)

    return answer-1

clothes = [["yellow_hat", "headgear"], ["blue_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "pants"], ["green_turban", "coat"]]

a = solution(clothes)

print(a)