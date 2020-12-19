from collections import defaultdict
import itertools


n_list = [12, 12, 1]
week_list = [[1, 5, 6, 10], [1, 3, 4, 9, 10], [0]]
dist_list = [[1, 2, 3, 4], [3, 5, 7], [100]]
result_list = [2, 1]


def solution(n, weak, dist):
    dist_per = []

    weak_circle = weak + [n + w for w in weak]
    del weak_circle[len(weak_circle) - 1] # 맨 마지막 원소 삭제

    min_value = 500

    for i in range(1, len(dist)+1):
        dist_per.extend(list(itertools.permutations(dist, i)))

    for start in range(0, len(weak)):
        for dist_tmp in dist_per:
            dist_len = len(dist_tmp)

            i = 0
            cur = -1

            check = True

            for num in range(len(weak)):
                if cur < weak_circle[start + num]:
                    if i < dist_len:
                        cur = weak_circle[start + num] + dist_tmp[i]
                        i = i + 1
                    else:
                        check = False
                        break
            if check:
                min_value = min(min_value, len(dist_tmp))

    answer = min_value

    if answer ==500:
        answer = -1

    return answer

for n, week, dist in zip(n_list, week_list, dist_list):
    ans = solution(n, week, dist)
    print(ans)