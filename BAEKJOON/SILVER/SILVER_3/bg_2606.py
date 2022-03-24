v, e = [int(input()) for _ in range(2)]

graph = [[] for _ in range(v+1)]
visited = [False] * (v+1)

for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(v):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

dfs(1)

result = -1
for i in range(1, v+1):
    if visited[i]:
        result += 1

print(result)