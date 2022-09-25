#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [0] * (10001)

# 계수정렬 O(N+K)
for _ in range(n):
    arr[int(input())] += 1

for i in range(10001):
    for _ in range(arr[i]):
        print(i, end='\n')