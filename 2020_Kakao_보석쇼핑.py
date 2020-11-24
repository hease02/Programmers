gems_list = [["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
             ["AA", "AB", "AC", "AA", "AC"],
             ["XYZ", "XYZ", "XYZ"], ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]]
result_list = [[3, 7],
               [1, 3],
                 [1, 1], [1, 5]]

def solution(gems):
    gems_count = set(gems)

    gems_size = len(gems_count) #gem 종류 개수

    gem_start = 0
    gem_end = 0
    gem_dict = {gems[0] : 1} #init

    gem_kind = 1

    answer = [0, len(gems)]

    while gem_end < len(gems) and gem_start < len(gems):
        if gem_kind == gems_size:
            if answer[1] - answer[0] > gem_end - gem_start:
                answer = [gem_start + 1, gem_end+1]

            gem_dict[gems[gem_start]] = gem_dict[gems[gem_start]] - 1

            if gem_dict[gems[gem_start]] is 0:
                del gem_dict[gems[gem_start]]
                gem_kind = gem_kind - 1

            gem_start = gem_start + 1

        else:
            gem_end = gem_end + 1

            if gem_end == len(gems):
                break

            if gems[gem_end] not in gem_dict.keys():
                gem_dict[gems[gem_end]] = 1
                gem_kind = gem_kind + 1
            else:
                gem_dict[gems[gem_end]] = gem_dict[gems[gem_end]] + 1

    return answer

for gem, result in zip(gems_list, result_list):
    ans = solution(gem)

    if ans is result:
        print("True")
    else:
        print("False - my_ans: {ans0}, {ans1}, but real_ans : {result0}, {result1}".format(ans0 = ans[0], ans1 = ans[1], result0 = result[0], result1 = result[1]))