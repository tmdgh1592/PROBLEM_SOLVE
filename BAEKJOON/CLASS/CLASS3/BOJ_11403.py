#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = [list(MIS()) for _ in range(n)]

# 플로이드 워셜 풀이
for k in range(n):
    for i in range(n):
         for j in range(n):
            if graph[i][j]: continue
            graph[i][j] = graph[i][k] * graph[k][j]

for i in range(n): print(*graph[i])