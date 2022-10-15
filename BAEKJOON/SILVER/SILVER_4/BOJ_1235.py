#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]

for size in range(1, len(arr[0]) + 1):
    dict_for_check = defaultdict(bool)
    for num in arr:
        num = num[:-size-1:-1]
        if dict_for_check[num]: break
        dict_for_check[num] = True
    else: break

print(size)