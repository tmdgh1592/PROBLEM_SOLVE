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
        if dist > distance[now]: continue
        
        for next, cost in graph[now]:
            new_cost = distance[now] + cost
            if new_cost < distance[next]:
                distance[next] = new_cost
                heapq.heappush(q, (new_cost, next))
    
    count, time = 0, - 1
    for i in range(1, n+1):
        if distance[i] != INF:
            count += 1
            time = max(time, distance[i])
    print(count, time)

for _ in range(int(input())):
    n, d, start = MIS()
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for _ in range(d):
        a, b, c = MIS()
        graph[b].append((a, c))
    
    dijkstra(start)