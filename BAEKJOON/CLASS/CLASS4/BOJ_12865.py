#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = -float('inf')

n, k = MIS()
data = [(0, 0)] + [tuple(MIS()) for _ in range(n)]
dp = [[0] * (k + 1) for _ in range(n + 1)] # 무게 i 만큼 채워 넣었을 때 최대 가치

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w, v = data[i]
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w] + v)

print(dp[n][k])