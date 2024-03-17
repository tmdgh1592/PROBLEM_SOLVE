from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []
    for i, order in enumerate(orders):
        orders[i] = ''.join(sorted(order))

    for c in course:
        mdict = defaultdict(int)

        for order in orders:
            if len(order) < c: continue
            combs = list(combinations(order, c))
            for comb in combs:
                mdict[''.join(comb)] += 1

        if not mdict: continue
        max_comb_cnt = sorted(mdict.values())[-1]
        for key, val in mdict.items():
            if val == max_comb_cnt and val > 1:
                answer.append(key)

    return sorted(answer)