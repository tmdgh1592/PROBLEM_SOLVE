#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

k, n = MIS()
arr = [int(input()) for _ in range(k)]

lo, hi = 1, max(arr)

def possible(length):
    cnt = 0
    for x in arr:
        cnt += (x // length)
        #print(x, length, x//length)
        if cnt >= n:
            return True
    
    return False


while lo <= hi:
    mid = (lo+hi) // 2
    if possible(mid):
        lo = mid + 1
    else:
        hi = mid - 1

print(hi)