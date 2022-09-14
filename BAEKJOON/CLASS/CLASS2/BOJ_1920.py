#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

find = defaultdict(int)

input()
for x in list(MIS()):
    find[x] = 1
input()
for x in list(MIS()):
    if find[x]:
        print(1)
    else:
        print(0)