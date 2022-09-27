#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def dfs(visited, now, dest, count):
    result = sys.maxsize

    if dest in graph[now]:
        return count

    visited[now] = True
    for next in graph[now]:
        if not visited[next]:
            result = min(result, dfs(visited, next, dest, count + 1))
    
    return result


n, m = MIS()
graph = [[] for _ in range(n+1)]
res, cost = 0, sys.maxsize

for _ in range(m):
    a, b = MIS()
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n+1):
    tmp_cost = 0

    for j in range(1, n+1):
        if i == j: continue
        
        visited = [False] * (n + 1)
        tmp_cost += dfs(visited, i, j, 1)

    if cost > tmp_cost:
        res = i; cost = tmp_cost

print(res)