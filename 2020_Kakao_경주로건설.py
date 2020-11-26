from collections import deque

# board_list = [[[0,0,0],[0,0,0],[0,0,0]],
#          [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]],
#          [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]],
#          [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]]
board_list = [[[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 1, 1, 0, 0]]]

#result_list = [900, 3800, 2100, 3200]
result_list = [3000]
class build:
    def __init__(self, posi_x, posi_y, cost, prevPosi):
        self.posi_x = posi_x
        self.posi_y = posi_y
        self.cost = cost
        self.prevPosi = prevPosi

def positionCheck(cur_posi,next_posi):
    if cur_posi == 0: #하
        if next_posi == 2 or next_posi == 3:
            return False #600
        else:
            return True # 100
    elif cur_posi == 1: #
        if next_posi == 2 or next_posi == 3:
            return False
        else:
            return True
    elif cur_posi == 2:#
        if next_posi == 0 or next_posi == 1:
            return False
        else:
            return True
    elif cur_posi == 3: #
        if next_posi == 0 or next_posi == 1:
            return False
        else:
            return True

def bfs(cur, board):
    que = deque()
    que.append(cur)

    posi_x = [0, 0, 1, -1] #하, 상, 우, 좌 (0, 1, 2, 3)
    posi_y = [1, -1, 0, 0]

    visit = [[0 for _ in range(len(board))] for _ in range(len(board))]

    for i in range(0, len(board)):
        for j in range(0, len(board)):
            visit[i][j] = board[i][j]

    while len(que) > 0:
        cur = que.popleft()

        cur_x = cur.posi_x
        cur_y = cur.posi_y

        for i in range(0, 4):
            x = cur_x + posi_x[i]
            y = cur_y + posi_y[i]

            if x >= 0 and y >= 0 and x < len(board) and y < len(board) and board[x][y] != 1:
                new_cost = 0

                if positionCheck(cur.prevPosi, i):
                    new_cost = cur.cost + 100
                else:
                    new_cost = cur.cost + 600

                if visit[x][y] == 0 or visit[x][y] > new_cost:
                    visit[x][y] = new_cost
                    cur_board = build(x, y, new_cost, i)
                    que.append(cur_board)

    return visit[len(board)-1][len(board)-1]

def solution(board):

    cur1 = build(0, 0, 0, 0)
    cur2 = build(0, 0, 0, 2)
    #answer = bfs(cur1)
    answer = min(bfs(cur1, board), bfs(cur2, board))

    return answer

for board, result in zip(board_list, result_list):
    ans = solution(board)

    if ans == result:
        print("True!")
    else:
        print("False - my ans: {my}, real ans: {re}".format(my=ans, re=result))