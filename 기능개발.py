import queue

def solution(progresses, speeds):
    answer = []

    q = []
    for p, s in zip(progresses, speeds):
        count = int((100 - p) / s)

        if (100 - p) % s > 0:
            count = count + 1

        q.append(count)

    top = q.pop(0)
    cnt = 1

    while len(q) > 0:
        if q[0] <= top:
            cnt = cnt + 1
            del q[0]
        else:
            top = q[0]
            answer.append(cnt)
            cnt = 0

    answer.append(cnt)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]

answer = solution(progresses, speeds)
print(answer)