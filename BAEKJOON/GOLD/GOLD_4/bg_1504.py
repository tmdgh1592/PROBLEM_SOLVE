import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (v+1)

    q = []
    heapq.heappush(q, (0, start))
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


v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


d1, d2 = map(int, input().split())

dist1 = dijkstra(1)
dist_d1 = dijkstra(d1)
dist_d2 = dijkstra(d2)


min_dist = min(dist1[d1]+dist_d1[d2]+dist_d2[v],
               dist1[d2]+dist_d2[d1]+dist_d1[v])

print(min_dist if min_dist < INF else -1)
