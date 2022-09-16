#-*- coding:utf-8 -*-
import sys
from typing import Counter

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

input()
l = Counter(MIS())
input()
arr = list(MIS())
for i, x in enumerate(arr):
    if i == len(arr)-1:
        ch_end = ''
    else:
        ch_end = ' '
    if x not in l:
        print(0, end=ch_end)
    else:
        print(l[x], end=ch_end)