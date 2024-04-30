from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def solution(rectangle, characterX, characterY, itemX, itemY):
    graph = [[-1] * 102 for _ in range(102)]
    visited = [[False] * 102 for _ in range(102)]
    visited[characterX * 2][characterY * 2] = True

    for rect in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rect)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                elif graph[i][j] != 0:
                    graph[i][j] = 1

    q = deque([(characterX * 2, characterY * 2, 0)])
    while q:
        x, y, move = q.popleft()

        if x == itemX * 2 and y == itemY * 2:
            return move // 2

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if graph[nx][ny] == 1 and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, move + 1))