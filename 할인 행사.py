from collections import defaultdict


def solution(want, number, discount):
    def check(discounts):
        for key, val in wants.items():
            if not discounts.get(key): return False
            if discounts[key] < val: return False
        return True

    wants = {want[i]: number[i] for i in range(len(want))}
    discounts = defaultdict(int)

    for i in range(sum(number)):
        discounts[discount[i]] += 1

    answer = int(wants == discounts)
    s, e = 0, sum(number) - 1

    while e < len(discount) - 1:
        discounts[discount[s]] -= 1
        if discounts[discount[s]] <= 0:
            del discounts[discount[s]]

        s += 1
        e += 1
        discounts[discount[e]] += 1
        answer += check(discounts)

    return answer