import heapq

INF = int(1e9)


def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    distance = [INF for _ in range(n + 1)]

    for x, y in roads:
        graph[x].append(y)
        graph[y].append(x)

    q = [(0, destination)]
    distance[destination] = 0

    while q:
        cost, now = heapq.heappop(q)

        if cost > distance[now]:
            continue

        for next in graph[now]:
            next_cost = cost + 1
            if next_cost < distance[next]:
                distance[next] = next_cost
                heapq.heappush(q, (next_cost, next))

    return [-1 if distance[s] == INF else distance[s] for s in sources]