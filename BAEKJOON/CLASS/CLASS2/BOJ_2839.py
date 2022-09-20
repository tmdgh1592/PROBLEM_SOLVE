#-*- coding:utf-8 -*-
import sys
INF = sys.maxsize

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

dp = [INF] * (5001)
dp[3], dp[4], dp[5] = (1, INF, 1)

for i in range(6, n+1):
    dp[i] = min(dp[i], dp[i-3] + 1, dp[i-5] + 1)

print(dp[n]) if dp[n] != INF else print(-1)