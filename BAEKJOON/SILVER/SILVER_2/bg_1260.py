from collections import deque

v, e, start = map(int, input().split())

visited = [False] * (v+1)
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for arr in graph:
    arr.sort()


def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for x in graph[v]:
        if not visited[x]:
            dfs(x)


def bfs(start):
    q = deque([start])
    visited[start] = True

    while q:
        now = q.popleft()
        print(now, end=' ')

        for x in graph[now]:
            if not visited[x]:
                q.append(x)
                visited[x] = True


dfs(start)
visited = [False] * (v+1)
print()
bfs(start)
