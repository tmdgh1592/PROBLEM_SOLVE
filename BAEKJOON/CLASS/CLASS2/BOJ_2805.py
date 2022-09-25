#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = list(MIS())
lo, hi = 0, max(arr)

while lo <= hi:
    mid = (lo + hi) // 2
    count = 0

    for x in arr:
        if x > mid: count += x-mid
        if count >= m: break

    if count >= m: lo = mid + 1
    else: hi = mid - 1

print(hi)