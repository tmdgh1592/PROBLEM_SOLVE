#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(MIS())
no_dupl_arr = sorted(list(set(arr)))
mdict = defaultdict(int)

for i, val in enumerate(no_dupl_arr):
    mdict[val] = i

for x in arr:
    print(mdict[x], end=' ')