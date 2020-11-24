answer = 0



def solution(numbers, target):
    answer = 0

    def dfs(numbers, target, idx, total, answer):
        if idx == len(numbers):
            if target == total:
                answer += 1
            return answer

        dfs(numbers, target, idx + 1, total + numbers[idx], answer)
        dfs(numbers, target, idx + 1, total - numbers[idx], answer)


    answer = dfs(numbers, target, 0, 0, answer)

    return answer

a = solution([1, 1, 1, 1, 1], 3)
print(a)