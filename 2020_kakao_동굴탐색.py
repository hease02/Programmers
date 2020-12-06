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
    if start in order_dict.keys():
        if order_check[order_dict[start]]:
            visit[start] = 1
        else:
            next_visit[start] = 1
            return
    else:
        if start in order_check.keys():
            order_check[start] = True

        visit[start] = 1

    for child in adj_list[start]:
        if visit[child] is not 1:
            dfs(child)
        else:
            if next_visit[child] is 1:
                dfs(child)

    return

def solution(n, path, order):
    global visit, next_visit, order_dict, order_check, adj_list

    answer = True

    adj_list = [[] for _ in range(n)]

    order_dict = {}
    order_check = {}

    visit = [0 for _ in range(n)] # 방문 확인용
    next_visit = [0 for _ in range(n)]

    #인접리스트 만들기
    for path_tmp in path:
        adj_list[path_tmp[0]].append(path_tmp[1])
        adj_list[path_tmp[1]].append(path_tmp[0])

    #order확인용 dict 만들기
    for order_tmp in order:
        order_dict[order_tmp[1]] = order_tmp[0] #order_dict[end] = start
        order_check[order_tmp[0]] = False

    for i in range(n):
        if visit[i] is not 1:
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