import sys
import heapq
input = sys.stdin.readline

INF = int(1e9)
n, t = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance = [INF] * (n+1)
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance


for _ in range(t):
    a, b = map(int, input().split())
    print(dijkstra(a)[b])
