import heapq

INF = int(1e9)


def solution(n, paths, gates, summits):
    graph = [[] for _ in range(n + 1)]
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    summits = set(summits)

    distance = [INF] * (n + 1)
    q = []
    for start in gates:
        distance[start] = 0
        heapq.heappush(q, [0, start])

    while q:
        dist, now = heapq.heappop(q)

        if now in summits or dist > distance[now]:
            continue

        for next, w in graph[now]:
            w = max(distance[now], w)
            if distance[next] > w:
                distance[next] = w
                heapq.heappush(q, [w, next])

    answer = [INF, INF]
    for summit in sorted(summits):
        if distance[summit] < answer[1]:
            answer = [summit, distance[summit]]
    return answer