#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = []
counts = []
friends = [[False] * n for _ in range(n)]
for i in range(n):
    row = list(input().rstrip())
    count = 0
    for j, ch in enumerate(row):
        if ch == 'Y':
            count += 1
            friends[i][j] = True
    counts.append(count)
    graph.append(row)

for i in range(n):
    for j in range(n):
        if i == j: continue
        if graph[i][j] == 'Y':
            for k in range(n):
                if i == k: continue
                if graph[k][j] == 'Y':
                    if not friends[i][k]:
                        friends[i][k] = True
                        counts[i] += 1

print(max(counts))