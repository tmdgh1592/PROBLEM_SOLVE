#-*- coding:utf-8 -*-
import heapq
import sys

input = sys.stdin.readline

q = []
for _ in range(int(input())):
    num = int(input())
    if num: heapq.heappush(q, num)
    else: print(heapq.heappop(q) if q else 0)