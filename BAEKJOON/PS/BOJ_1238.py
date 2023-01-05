#-*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = int(1e9)

def dijkstra(start):
    q = [(0, start)]
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        
        if dist < distance[now]: continue

        for next, cost in graph[now]:
            new_next_distance = dist + cost
            if new_next_distance < distance[next]:
                distance[next] = new_next_distance
                heapq.heappush(q, (new_next_distance, next))


n, m, dest = MIS()
graph = [[] for _ in range(n + 1)]
costs = [0 for _ in range(n + 1)]
res = 0

for _ in range(m):
    a, b, c = MIS()
    graph[a].append((b, c))

for i in range(1, n+1):
    distance = [INF] * (n + 1)
    dijkstra(i)
    costs[i] = distance[dest]

distance = [INF] * (n + 1)
dijkstra(dest)
for i in range(1, n+1):
    costs[i] += distance[i]
    res = max(res, costs[i])

print(res)