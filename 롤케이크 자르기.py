from collections import defaultdict, Counter


def solution(topping):
    answer = 0
    a, b = defaultdict(int), Counter(topping)

    if len(topping) == 1: return 0

    for i in range(len(topping)):
        a[topping[i]] += 1
        b[topping[i]] -= 1
        if b[topping[i]] <= 0:
            del b[topping[i]]

        if len(a.keys()) == len(b.keys()):
            answer += 1

    return answer