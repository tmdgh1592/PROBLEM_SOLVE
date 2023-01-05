#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def check(k):
    count = 1
    curr_money = k
    for x in arr:
        if x > curr_money:
            count += 1
            curr_money = k
        curr_money -= x

    return count <= m


n, m = MIS()
arr = [int(input()) for _ in range(n)]
lo, hi = max(arr), 1000000000

while lo <= hi:
    mid = (lo + hi) // 2
    if check(mid): hi = mid - 1
    else: lo = mid + 1

print(lo)