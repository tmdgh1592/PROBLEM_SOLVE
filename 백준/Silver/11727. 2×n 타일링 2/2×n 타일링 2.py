#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e9))

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
dp = [0] * (1001)
dp[1], dp[2] = 1, 3

def f(i):
    if dp[i] != 0:
        return dp[i] % 10007
    dp[i] = (f(i-1) + 2 * f(i-2)) % 10007
    return dp[i]

print(f(n))