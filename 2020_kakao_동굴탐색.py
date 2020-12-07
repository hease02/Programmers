import sys
sys.setrecursionlimit(10**9)

n_list = [9, 9, 9]
path_list = [[[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]],
             [[8, 1], [0, 1], [1, 2], [0, 7], [4, 7], [0, 3], [7, 5], [3, 6]],
             [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]]
order_list = [[[8, 5], [6, 7], [4, 1]],
              [[4, 1], [5, 2]],
              [[4, 1], [8, 7], [6, 5]]]
result_list = [True, True, False]

def dfs(start):
    #order를 확인하여 visit / next_visit 표시
    if visit[start]: #방문했을 경우 바로 리턴
        return

    if start in order_dict.keys():
        if visit[order_dict[start]] is not 1:
            next_visit[order_dict[start]] = start
            return

    visit[start] = 1

    if next_visit[start] is not -1:
        dfs(next_visit[start])

    for child in adj_list[start]:
        dfs(child)

    return

def solution(n, path, order):
    global visit, next_visit, order_dict, order_check, adj_list

    answer = True

    adj_list = [[] for _ in range(n)]

    order_dict = {}
    order_check = {}

    visit = [0 for _ in range(n)] # 방문 확인용
    next_visit = [-1 for _ in range(n)]

    #인접리스트 만들기
    for path_tmp in path:
        adj_list[path_tmp[0]].append(path_tmp[1])
        adj_list[path_tmp[1]].append(path_tmp[0])

    #order확인용 dict 만들기
    for order_tmp in order:
        order_dict[order_tmp[1]] = order_tmp[0] #order_dict[end] = start

    if 0 in order_dict.keys():
        return False

    visit[0] = 1

    for i in adj_list[0]:
        dfs(i)

    for ans in visit:
        if ans == 0:
            answer = False

    return answer


for n, path, order, result in zip(n_list, path_list, order_list, result_list):
    ans = solution(n, path, order)

    if ans is result:
        print("Success")
    else:
        print("Fail")