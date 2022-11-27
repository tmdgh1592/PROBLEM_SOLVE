#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = float('inf')

a, b = MIS()


def f(now, cnt):
    if now > b:
        return INF
    if now == b:
        return cnt
    
    res = min(INF, f(now * 2, cnt + 1), f(now * 10 + 1, cnt + 1))
    return res

res = f(a, 1)
print(-1 if res == INF else res)