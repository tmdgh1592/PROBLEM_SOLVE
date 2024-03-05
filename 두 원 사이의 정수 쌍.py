from math import floor, ceil


def solution(r1, r2):
    answer = 0

    for x in range(1, r2 + 1):
        a = 0 if x >= r1 else ceil((r1 ** 2 - x ** 2) ** 0.5)
        b = ceil((r2 ** 2 - x ** 2) ** 0.5)
        answer += b - a

    return answer * 4