#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

res = 0
n, m = MIS()
k, *arr = MIS()
knowns = set(arr)
parties = [set(list(MIS())[1:]) for _ in range(m)]

for _ in range(m):
    for party in parties:
        if knowns & party:
            knowns |= party

for party in parties:
    if party & knowns: continue
    res += 1

print(res)