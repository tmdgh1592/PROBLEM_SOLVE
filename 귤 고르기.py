from collections import Counter


def solution(k, tangerine):
    answer = 0

    counter = sorted(Counter(tangerine).values(), reverse=True)

    for val in counter:
        k -= val
        answer += 1
        if k <= 0: return answer
