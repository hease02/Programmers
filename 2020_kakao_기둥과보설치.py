n_list = [5, 5]
build_frame_list = [[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
                    [[0, 0, 0, 1], [2, 0, 0, 1], [4, 0, 0, 1], [0, 1, 1, 1], [1, 1, 1, 1], [2, 1, 1, 1], [3, 1, 1, 1],
                     [2, 0, 0, 0], [1, 1, 1, 0], [2, 2, 0, 1]]]
result_list = [[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]],
               [[0, 0, 0], [0, 1, 1], [1, 1, 1], [2, 1, 1], [3, 1, 1], [4, 0, 0]]]

def buildWall(build, pillar, wrap, n):
    x, y, a = build

    if a == 0: #기둥
        if (y == 0) or (y > 0 and (pillar[x][y-1] == 1)) or ((x > 0 and wrap[x-1][y] == 1) or (wrap[x][y] == 1)):
            return True
    elif a == 1 : #보
        if ((y > 0 and (pillar[x][y-1] == 1) ) or (y > 0 and (pillar[x+1][y-1] == 1))) or ( (x > 0 and wrap[x-1][y] == 1) and (x < n and wrap[x+1][y] == 1)):
            return True

    return False

def buildCheck(result, pillar, wrap ,n):
    for build in result:
        if not buildWall(build, pillar, wrap, n):
            return False
    return True

def insertBuild(build, pillar, wrap, install):
    x, y, a = build
    if a == 0:
        pillar[x][y] = install
    elif a == 1:
        wrap[x][y] = install

def solution(n, build_frame):
    answer = []

    pillar = [[0 for _ in range(n+1)] for _ in range(n+1)]
    wrap = [[0 for _ in range(n+1)] for _ in range(n+1)]

    for x, y, a, b in build_frame:
        if b == 1: # 건설
            if buildWall([x, y, a], pillar, wrap, n):
                insertBuild([x, y, a], pillar, wrap, b)
                answer.append([x, y, a])

        elif b == 0: #삭제
            insertBuild([x, y, a], pillar, wrap, b)

            if buildCheck(answer, pillar, wrap, n):
                answer.remove([x, y, a])
            else:
                insertBuild([x, y, a], pillar, wrap, 1)

    answer = sorted(answer, key=lambda x : (x[0], x[1], x[2]))

    return answer

for n, build, result in zip(n_list, build_frame_list, result_list):
    print(solution(n, build))