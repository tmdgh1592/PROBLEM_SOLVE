def solution(a):
    answer = 0

    left, right = float('inf'), float('inf')
    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            answer += 1
        if a[-1 - i] < right:
            right = a[-1 - i]
            answer += 1

    return answer - 1