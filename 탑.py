def solution(heights):
    heights = list(reversed(heights))
    answer = [0 for i in range(len(heights))]

    index = 0

    for i in range(0, len(heights)):
        cur = heights[0]
        del heights[0]
        temp = []

        for j in range(0, len(heights)):
            if heights[0] > cur:
                answer[index] = len(heights)
                break
            else:
                temp.append(heights[0])
                del heights[0]

        index = index+1

        if len(temp) > 0:
            heights = temp + heights

    answer = list(reversed(answer))
    return answer

heights = [6,9,5,7,4]
#heights = [1,5,3,6,7,6,5]
#heights = [3,9,9,3,5,7,2]
answer = solution(heights)
print(answer)
