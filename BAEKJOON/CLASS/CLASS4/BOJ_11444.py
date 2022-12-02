#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

DIVIDER = 1000000007
n = int(input())
dp = dict()

def fibo(x):
    if dp.get(x) != None:
        return dp[x]
    if x == 0:
        return 0
    if x == 1 or x == 2:
        return 1
    if x % 2 == 0:
        dp[x // 2 + 1] = fibo(x // 2 + 1) % DIVIDER
        dp[x // 2 - 1] = fibo(x // 2 - 1) % DIVIDER
        return dp[x // 2 + 1] ** 2 - dp[x // 2 - 1] ** 2
    else:
        dp[x // 2 + 1] = fibo(x // 2 + 1) % DIVIDER
        dp[x // 2] = fibo(x // 2) % DIVIDER
        return dp[x // 2 + 1] ** 2 + dp[x // 2] ** 2

print(fibo(n) % DIVIDER)