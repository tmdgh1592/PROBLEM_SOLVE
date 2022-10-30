#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
data = [list(MIS()) for _ in range(n)]
cache = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        cache[i][j] = cache[i-1][j] + cache[i][j-1] - cache[i-1][j-1] + data[i-1][j-1]

for _ in range(m):
    x1, y1, x2, y2 = MIS()
    print(cache[x2][y2] - cache[x1-1][y2] - cache[x2][y1-1] + cache[x1-1][y1-1])