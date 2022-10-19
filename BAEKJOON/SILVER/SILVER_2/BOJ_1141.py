#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())
arr = sorted([input().rstrip() for _ in range(n)], key=len)
res = 0

for i, word in enumerate(arr):
    for other in arr[i+1:]:
        if other.startswith(word): break
    else: res += 1

print(res)