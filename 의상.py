from collections import defaultdict


def solution(clothes):
    answer = 1
    mdict = defaultdict(int)

    for _, typ in clothes:
        mdict[typ] += 1

    for x in mdict.values():
        answer *= (x + 1)

    return answer - 1