#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

nope = defaultdict(int)
result = []
total = 0

n, m = MIS()
for person in range(n + m):
    nope[input().rstrip()] += 1

for name, cnt in nope.items():
    if cnt == 2:
        result.append(name)
        total += 1

print(total, *sorted(result), sep='\n')