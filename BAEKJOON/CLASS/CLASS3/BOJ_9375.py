#-*- coding:utf-8 -*-
from collections import defaultdict
from functools import reduce
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
ONE_PLUS = lambda x: x + 1

for _ in range(int(input())):
    n = int(input())
    mdict = defaultdict(int)

    for _ in range(n):
        _, type = input().rstrip().split()
        mdict[type] += 1
    
    print(reduce(lambda x, y: x * y, map(ONE_PLUS, mdict.values()), 1) - 1)