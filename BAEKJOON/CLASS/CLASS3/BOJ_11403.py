#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = [set() for _ in range(n)]

def append(visited, start, idx):
    if not graph[idx]:
        visited[idx] = True
        return

    visited[idx] = True
    next_list = graph[idx]
    graph[start] = graph[start].union(next_list)

    for next in next_list:
        if not visited[next]:
            visited[next] = True
            append(visited, start, next)


for i in range(n):
    row = list(MIS())
    for j, val in enumerate(row):
        if val: graph[i].add(j)

for i in range(n):
    for idx in graph[i]:
        visited = [False] * (n)
        append(visited, i, idx)

for i in range(n):
    for j in range(n):
        end_ch = '\n' if j == n-1 else ' '

        if j in graph[i]: print(1, end=end_ch)
        else: print(0, end=end_ch)