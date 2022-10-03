def solution(numbers):
    answer = 45
    for num in numbers:
        answer -= num
    return answer