#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def possible(mid, money):
    # 요청한 예산을 모두 고려할 수 없는 경우 상한선(mid) 체크
    total = 0
    for x in arr:
        if x < mid: total += x
        else: total += mid

    return total <= money

n = int(input())
arr = sorted(list(MIS()))
lo, hi = 0, arr[-1]
money = int(input())

while lo <= hi:
    mid = (lo + hi) // 2
    if possible(mid, money): lo = mid + 1
    else: hi = mid - 1

print(hi)