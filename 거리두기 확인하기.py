from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < 5 and 0 <= y < 5


def bfs(graph, sx, sy):
    q = deque([(sx, sy, 0)])
    visited = [[False] * 5 for _ in range(5)]
    visited[sx][sy] = True

    while q:
        x, y, move = q.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(nx, ny): continue
            if visited[nx][ny]: continue
            if graph[nx][ny] == 'X': continue
            if graph[nx][ny] == 'P' and move + 1 <= 2: return False
            q.append((nx, ny, move + 1))
            visited[nx][ny] = True

    return True


def check(graph):
    people = []
    for i in range(5):
        for j in range(5):
            if graph[i][j] == 'P':
                people.append((i, j))

    for x, y in people:
        if not bfs(graph, x, y): return 0
    return 1


def solution(places):
    return [check(place) for place in places]