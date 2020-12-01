import copy

def rotate(key):
    ret=[]
    m=len(key)
    for i in range(4):
        temp = [[0 for i in range(m)] for j in range(m)]
        for i in range(m):
            for j in range(m):
                temp[m-j-1][i]=key[i][j]
        key = temp
        ret.append(temp)

    return ret

def solution(key, lock):
    answer = False

    key_list = rotate(key)
    lock_list = [[0 for _ in range(0, 60)] for _ in range(0, 60)]

    for i in range(len(key)-1, len(key) + len(lock) -1):
        for j in range(len(key)-1, len(key) + len(lock) -1):
            lock_list[i][j] = lock[i - len(key) +1][j - len(key) + 1]

    for i in range(0, len(key) + len(lock) - 1):
        for j in range(0, len(key) + len(lock) - 1):

            for key_temp in key_list:
                lock_temp = copy.deepcopy(lock_list)

                for n in range(0, len(key)):
                    for m in range(0, len(key)):
                        if ((len(key) - 1) <= (i + n) < (len(key) + len(lock) -1)) and ((len(key) - 1) <= (j + m) < (len(key) + len(lock) -1)) :
                            lock_temp[i + n][j + m] = lock_temp[i + n][j + m] + key_temp[n][m]

                result = True

                for a in range(len(key)-1, len(key) + len(lock) -1):
                    for b in range(len(key)-1, len(key) + len(lock) -1):
                        if lock_temp[a][b] != 1:
                            result = False
                            break
                    if not result:
                        break

                if result:
                    return True

    return answer