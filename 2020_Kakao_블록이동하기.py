from collections import deque
import sys

class Robot:
    def __init__(self, blk1_x, blk1_y, blk2_x, blk2_y, horizon, move):
        self.blk1_x = blk1_x
        self.blk1_y = blk1_y
        self.blk2_x = blk2_x
        self.blk2_y = blk2_y
        self.horizon = horizon
        self.move = move

def solution(board):
    answer = sys.maxsize

    que = deque()


    normal_dir = [[-1, 0, -1, 0], [1, 0, 1, 0], [0, 1, 0, 1], [0, -1, 0, -1]] #상하우좌

    horizon_rotate = [[[1, 0, 1, 0], [0, 1, 1, 0]],
                      [[1, 0, 1, 0], [0, 0, 1, -1]],
                      [[-1, 0, -1, 0], [-1, 0, 0, -1]],
                      [[-1, 0, -1, 0], [-1, 1, 0, 0]]]
    vertical_rotate = [[[0, 1, 0, 1], [0, 0, -1, 1]],
                       [[0, 1, 0, 1], [1, 0, 0, 1]],
                       [[0, -1, 0, -1], [1, -1, 0, 0]],
                       [[0,-1, 0, -1], [0, -1, -1, 0]]]


    que.append(Robot(0, 0, 0, 1, True, 0))

    visited = [[0, 0, 0, 1]]
    board_len = len(board)

    visited_dict = {0:0}

    while len(que) > 0:
        robot = que.popleft()

        if (robot.blk1_x == board_len -1 and robot.blk1_y == board_len-1) or (robot.blk2_x == board_len -1 and robot.blk2_y == board_len-1):
            answer = min(answer, robot.move)

        for dir in normal_dir:
            dir1_x = robot.blk1_x + dir[0]
            dir1_y = robot.blk1_y + dir[1]
            dir2_x = robot.blk2_x + dir[2]
            dir2_y = robot.blk2_y + dir[3]

            if 0 <= dir1_x < board_len and 0 <= dir1_y < board_len and 0 <= dir2_x < board_len and 0 <= dir2_y < board_len:
                if board[dir1_x][dir1_y] == 0 and board[dir2_x][dir2_y] == 0:
                    add_robot = Robot(dir1_x, dir1_y, dir2_x, dir2_y, robot.horizon, robot.move + 1)
                    if [dir1_x, dir1_y, dir2_x, dir2_y] in visited:
                        if visited_dict[visited.index([dir1_x, dir1_y, dir2_x, dir2_y])] > robot.move + 1:
                            visited_dict[visited.index([dir1_x, dir1_y, dir2_x, dir2_y])] = robot.move + 1
                            que.append(add_robot)
                    else:
                        visited.append([dir1_x, dir1_y, dir2_x, dir2_y])
                        visited_dict[visited.index([dir1_x, dir1_y, dir2_x, dir2_y])] = robot.move + 1
                        que.append(add_robot)
        if robot.horizon:
            for rotate in horizon_rotate:
                dir1_x = robot.blk1_x + rotate[0][0]
                dir1_y = robot.blk1_y + rotate[0][1]
                dir2_x = robot.blk2_x + rotate[0][2]
                dir2_y = robot.blk2_y + rotate[0][3]

                rot_dir1_x = robot.blk1_x + rotate[1][0]
                rot_dir1_y = robot.blk1_y + rotate[1][1]
                rot_dir2_x = robot.blk2_x + rotate[1][2]
                rot_dir2_y = robot.blk2_y + rotate[1][3]

                if 0 <= dir1_x < board_len and 0 <= dir1_y < board_len and 0 <= dir2_x < board_len and 0 <= dir2_y < board_len:
                    if board[dir1_x][dir1_y] == 0 and board[dir2_x][dir2_y] == 0:

                        add_robot = Robot(rot_dir1_x, rot_dir1_y, rot_dir2_x, rot_dir2_y, False, robot.move + 1)
                        rot_dir = [rot_dir1_x, rot_dir1_y, rot_dir2_x, rot_dir2_y]
                        if rot_dir in visited:
                            if visited_dict[visited.index(rot_dir)] > robot.move + 1:
                                visited_dict[visited.index(rot_dir)] = robot.move + 1
                                que.append(add_robot)
                        else:
                            visited.append(rot_dir)
                            visited_dict[visited.index(rot_dir)] = robot.move + 1
                            que.append(add_robot)

        else:
            for rotate in vertical_rotate:
                dir1_x = robot.blk1_x + rotate[0][0]
                dir1_y = robot.blk1_y + rotate[0][1]
                dir2_x = robot.blk2_x + rotate[0][2]
                dir2_y = robot.blk2_y + rotate[0][3]

                rot_dir1_x = robot.blk1_x + rotate[1][0]
                rot_dir1_y = robot.blk1_y + rotate[1][1]
                rot_dir2_x = robot.blk2_x + rotate[1][2]
                rot_dir2_y = robot.blk2_y + rotate[1][3]

                if 0 <= dir1_x < board_len and 0 <= dir1_y < board_len and 0 <= dir2_x < board_len and 0 <= dir2_y < board_len:
                    if board[dir1_x][dir1_y] == 0 and board[dir2_x][dir2_y] == 0:

                        add_robot = Robot(rot_dir1_x, rot_dir1_y, rot_dir2_x, rot_dir2_y, True, robot.move + 1)
                        rot_dir = [rot_dir1_x, rot_dir1_y, rot_dir2_x, rot_dir2_y]
                        if rot_dir in visited:
                            if visited_dict[visited.index(rot_dir)] > robot.move + 1:
                                visited_dict[visited.index(rot_dir)] = robot.move + 1
                                que.append(add_robot)
                        else:
                            visited.append(rot_dir)
                            visited_dict[visited.index(rot_dir)] = robot.move + 1
                            que.append(add_robot)

    return answer