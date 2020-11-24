def solution(numbers):
    numbers = list(map(str, numbers))

    answer = sorted(numbers, key= lambda a: (a[0:len(numbers)] + a))
    return answer

def cmp(a, b):
    return a + b

#numbers = [6, 10, 2]
numbers = [30, 3, 321, 32]
answer = solution(numbers)
print(answer)