from collections import deque


n = int(input())
graph = []
counts = []

for _ in range(n):
    graph.append(list(map(int, list(input()))))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(ix, iy):
    count = graph[ix][iy]
    q = deque()
    if graph[ix][iy] != 0:  # 방문하지 않은 노드부터 시작한다면
        q.append((ix, iy))  # Queue에 추가
        graph[ix][iy] = 0  # 방문처리

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if graph[nx][ny] == 1:
                    count += 1
                    q.append((nx, ny))  # Queue에 추가
                    graph[nx][ny] = 0  # 방문처리

    return count


for i in range(n):
    for j in range(n):
        count = bfs(i, j)
        if count != 0:
            counts.append(count)

print(len(counts))
[print(x) for x in sorted(counts)]
