def solution(citations):
    answer = 0
    sort_list = sorted(citations, reverse=True)
    index = 0

    while index <= len(sort_list):
        cnt = 0

        for n in range(0, len(sort_list)):
            if index <= sort_list[n]:
                cnt = cnt + 1

        if (cnt >= index) and (len(sort_list) - cnt <= index):
            answer = max(answer, index)

        index = index + 1

    return answer

#citations = [3, 0, 6, 1, 5]
citations = [4, 7, 4, 1, 6, 5, 2]

ans =solution(citations)
print(ans)