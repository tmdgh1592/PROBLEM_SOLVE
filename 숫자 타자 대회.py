from collections import defaultdict
import sys

sys.setrecursionlimit(int(1e9))
dp = defaultdict(lambda: int(1e9))  # key : (i, left, right)

weights = [
    [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
    [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
    [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
    [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
    [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
    [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
    [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
    [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
    [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
    [3, 6, 5, 4, 5, 3, 2, 4, 2, 1]
]


def solution(numbers):
    numbers = [int(num) for num in numbers]

    def f(i, left, right):
        if i == len(numbers):
            return 0
        if dp[(i, left, right)] != int(1e9):
            return dp[(i, left, right)]

        num = numbers[i]
        if numbers[i] != left:
            dp[(i, left, right)] = min(dp[(i, left, right)], f(i + 1, left, num) + weights[right][num])
        if numbers[i] != right:
            dp[(i, left, right)] = min(dp[(i, left, right)], f(i + 1, num, right) + weights[left][num])

        return dp[(i, left, right)]

    return f(0, 4, 6)
