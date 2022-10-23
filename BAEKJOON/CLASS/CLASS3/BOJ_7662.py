#-*- coding:utf-8 -*-
from collections import defaultdict
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    deleted = defaultdict(bool)
    left = [] # min heap
    right = [] # max heap
    for uni_key in range(int(input())):
        cmd, num = input().split()
        num = int(num)

        if cmd == 'I':
            heapq.heappush(left, (num, uni_key))
            heapq.heappush(right,(-num, uni_key))
        else:
            if num == -1:
                while left and deleted[left[0][1]]:
                    heapq.heappop(left)
                if left:
                    _, key = heapq.heappop(left)
                    deleted[key] = True
            else:
                while right and deleted[right[0][1]]:
                    heapq.heappop(right)
                if right:
                    _, key = heapq.heappop(right)
                    deleted[key] = True

    while left and deleted[left[0][1]]:
        heapq.heappop(left)
    while right and deleted[right[0][1]]:
        heapq.heappop(right)
    
    if left and right:
        print(-right[0][0], left[0][0])
    else:
        print('EMPTY')