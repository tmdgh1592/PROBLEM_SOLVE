#-*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    num = int(input())
    if num < 0:
        heapq.heappush(arr, (abs(num), -1))
    elif num > 0:
        heapq.heappush(arr, (abs(num), 1))
    else: # 0인 경우
        if not arr: print(0)
        else:
            val, v = heapq.heappop(arr)
            print(val * v)