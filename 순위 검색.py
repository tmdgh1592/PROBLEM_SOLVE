from bisect import bisect_left
from itertools import combinations
from collections import defaultdict

def parse_info(arr):
    mdict = defaultdict(list)
    for data in arr:
        a, b, c, d, e = data.split(' ')
        for i in range(5):
            mlist = combinations([a,b,c,d], i)
            for x in mlist:
                mdict[str(''.join(x))].append(int(e))
    return mdict

def parse_query(arr):
    res = []
    for data in arr:
        a = data.split(' and ')
        food, score = a[-1].split(' ')
        score = int(score)
        sen = ''.join(a[:3]).replace('-', '')
        if food != '-': sen += food
        res.append((sen, score))
    return res


def solution(infos, queries):
    mdict = parse_info(infos) # [점수, 언어, 분야, 경력, 음식]
    queries = parse_query(queries) # [점수, 언어, 분야, 경력, 음식]
    answer = []
    for query, scores in mdict.items():
        mdict[query] = sorted(scores)

    for query, score in queries:
        user_scores = mdict[query]
        answer.append(len(user_scores) - bisect_left(user_scores, score))
    return answer