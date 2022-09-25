#-*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    num = int(input())
    
    if not arr and num == 0: print(0)
    elif num == 0: print(-heapq.heappop(arr))
    else: heapq.heappush(arr, -num)