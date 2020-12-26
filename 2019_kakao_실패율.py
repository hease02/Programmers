from operator import itemgetter
N_list = [5, 4]
stages_list = [[2, 1, 2, 6, 2, 4, 3, 3], [4,4,4,4,4]]
result_list = [[3,4,2,1,5], [4,1,2,3]]


def solution(N, stages):
    result = []

    fail_list = [0 for _ in range(N+2)]
    fail_rate = [0 for _ in range(N+2)]

    for val in stages:
        fail_list[val] += 1

    player = len(stages)

    for idx, fail in enumerate(fail_list):
        if idx == 0:
            continue

        player = player - fail_list[idx-1]

        if player == 0:
            fail_rate[idx] = 0
        else:
            fail_rate[idx] = float(fail / player)


    del fail_rate[0]
    del fail_rate[len(fail_rate)-1]

    answer = sorted(enumerate(fail_rate), key=itemgetter(1), reverse=True)

    for ans in answer:
        result.append(ans[0] + 1)

    return result

for n, stage in zip(N_list, stages_list):
    ans = solution(n, stage)

    print(ans)