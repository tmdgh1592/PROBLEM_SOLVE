def solution(numbers):
    s = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while s and numbers[s[-1]] < numbers[i]:
            answer[s.pop()] = numbers[i]
        s.append(i)

    return answer