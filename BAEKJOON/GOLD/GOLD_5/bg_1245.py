from collections import deque


n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [([False] * m) for _ in range(n)]


def bfs(sx, sy):
    q = deque([(sx, sy)])
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    flag = True

    while q:
        x, y = q.popleft()
        visited[x][y] = True

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if (nx < 0 or ny < 0 or nx >= n or ny >= m):
                continue
            if not visited[nx][ny] and (graph[x][y] == graph[nx][ny]):
                q.append((nx, ny))
            if graph[x][y] < graph[nx][ny]:
                flag = False

    return flag


count = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if bfs(i, j):
                count += 1

print(count)
