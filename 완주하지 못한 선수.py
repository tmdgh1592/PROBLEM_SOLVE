from collections import defaultdict


def solution(participant, completion):
    mdict = defaultdict(int)
    for person in participant:
        mdict[person] += 1
    for person in completion:
        mdict[person] -= 1

    return sorted(mdict.items(), key=lambda x: -x[1])[0][0]