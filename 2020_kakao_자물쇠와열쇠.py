
key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]


def rotate(m, d):
    N = len(m)
    ret = [[0] * N for _ in range(N)]

    if d % 4 == 1:
        for r in range(N):
            for c in range(N):
                ret[c][N-1-r] = m[r][c]
    elif d % 4 == 2:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][N-1-r] = m[r][c]
    elif d % 4 == 3:
        for r in range(N):
            for c in range(N):
                ret[N-1-c][r] = m[r][c]
    else:
        ret = m

    return ret

def solution(key, lock):
    answer = False

    rotate_90 = rotate(key, 1)
    rotate_180 = rotate(key, 2)
    rotate_270 = rotate(key, 3)

    lock_list = [[2 for _ in range(0, 60)] for _ in range(0, 60)]

    for i in range(len(key)-1, len(key) + len(lock) -1):
        for j in range(len(key)-1, len(key) + len(lock) -1):
            lock_list[i][j] = lock[i - len(key) +1][j - len(key) + 1]


    for key_num in range(0, 4):
        # if key_num == 1 :
        #     key = rotate_90
        # elif key_num ==2 :
        #     key = rotate_180
        # elif key_num == 3:
        #     key = rotate_270

        for i in range(0, len(key) + len(lock) - 1):
            for j in range(0, len(key) + len(lock) - 1):
                result = True

                for n in range(0, len(key)):
                    if not result:
                        break

                    for m in range(0, len(key)):
                        if lock_list[i + n][j + m] == 2:
                            continue

                        if (lock_list[i + n][j + m] ^ key[n][m]) == 0:
                            result = False
                            break

                if result:
                    return True

    return answer

print(solution(key, lock))