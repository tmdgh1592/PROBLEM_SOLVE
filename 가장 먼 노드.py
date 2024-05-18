from collections import deque

INF = int(1e9)


def solution(n, edge):
    distance = [INF] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    q = deque([(1, 0)])
    distance[1] = 0
    while q:
        now, dist = q.popleft()

        if dist > distance[now]:
            continue

        for next, c in graph[now]:
            cost = dist + c
            if cost < distance[next]:
                distance[next] = cost
                q.append((next, cost))

    max_dist = sorted(distance, reverse=True)[1]
    return distance.count(max_dist)
