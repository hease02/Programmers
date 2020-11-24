import heapq

def scale(scov1, scov2):
    scov = scov1 + (scov2 * 2)
    return scov

def solution(scoville, K):
    answer = 0

    heapq.heapify(scoville)

    while scoville[0] < K:
        if len(scoville) == 1:
            return -1

        min1 = heapq.heappop(scoville)
        min2 = heapq.heappop(scoville)

        scov_scale = scale(min1, min2)
        answer += 1

        heapq.heappush(scoville, scov_scale)

    return answer

scoville = [12, 2, 9, 3, 10, 1]
K = 7

answer = solution(scoville, K)
print(answer)