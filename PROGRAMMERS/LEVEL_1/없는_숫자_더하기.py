def solution(numbers):
    answer = 0

    for num in range(0, 10):
        if num not in numbers:
            answer += num
    return answer
