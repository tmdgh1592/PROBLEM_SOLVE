#-*- coding:utf-8 -*-
import heapq
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = int(1e9)

def dijkstra(block_a, block_b):
    distance = [INF] * (n+1)
    path = []
    q = [(0, 1)]
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]: continue

        for next, cost in graph[now]:
            if now == block_a and next == block_b: continue

            next_cost = distance[now] + cost
            if next_cost < distance[next]:
                path.append((now, next))
                distance[next] = next_cost
                heapq.heappush(q, (next_cost, next))

    return (distance[n], path)


n, m = MIS()
graph = [[] for _ in range(n+1)]

# 블럭 대상
# 가중치가 가장 작은 간선
# 마지막 노드와 연결되어 있는 간선
min_weight = sys.maxsize
for _ in range(m):
    a, b, c = MIS()
    graph[a].append((b, c))
    graph[b].append((a, c))

origin, block = dijkstra(0, 0)
res = 0
for a, b in block:
    blocked = dijkstra(a, b)
    if blocked[0] == INF:
        print(-1)
        break
    else:
        res = max(res, blocked[0] - origin)
else:
    print(res)