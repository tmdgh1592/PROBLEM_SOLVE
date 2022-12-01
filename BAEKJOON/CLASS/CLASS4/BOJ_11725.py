# -*- coding:utf-8 -*-
import sys
from collections import deque

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def MIS(): return map(int, input().rstrip().split())


n = int(input())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)
visited = [False] * (n + 1)
q = deque([1])

for _ in range(n - 1):
    a, b = MIS()
    graph[a].append(b)
    graph[b].append(a)

while q:
    node = q.popleft()
    visited[node] = True

    for next in graph[node]:
        if not visited[next]:
            parent[next] = node
            visited[next] = True
            q.append(next)

print(*parent[2:], sep='\n')