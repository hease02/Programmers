import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    num = 0
    priorityQ = []

    while stock < k :
        for i in range(num, len(dates)):
            if stock < dates[i]:
                break
            heapq.heappush(priorityQ, supplies[i] * (-1))
            num = i + 1

        stock = stock + (heapq.heappop(priorityQ) * (-1))
        answer = answer + 1

    return answer


dates = [4,10,15]
supplies = [20,5,10]

answer = solution(4, dates, supplies, 30)

print(answer)