from collections import defaultdict
import itertools

n_list = [12, 12]
week_list = [[1, 5, 6, 10], [1, 3, 4, 9, 10]]
dist_list = [[1, 2, 3, 4], [3, 5, 7]]
result_list = [2, 1]


def solution(n, weak, dist):
    answer = 0

    dist_dict = defaultdict(list)

    for n in range(len(dist)):
        dist_dict[n] = itertools.combinations(dist, n)



    return answer

for n, week, dist in zip(n_list, week_list, dist_list):
    ans = solution(n, week, dist)
    print(ans)