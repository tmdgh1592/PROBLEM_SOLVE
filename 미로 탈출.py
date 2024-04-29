from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m


def find(maps, n, m, sx, sy, goal):
    visited = [[False] * m for _ in range(n)]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while q:
        x, y, move = q.popleft()
        if maps[x][y] == goal:
            return move

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if not in_range(n, m, nx, ny): continue
            if maps[nx][ny] == 'X': continue
            if visited[nx][ny]: continue
            visited[nx][ny] = True
            q.append((nx, ny, move + 1))

    return int(1e9)


def solution(maps):
    sx, sy = 0, 0
    lx, ly = 0, 0
    n, m = len(maps), len(maps[0])

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx, sy = i, j
            elif maps[i][j] == 'L':
                lx, ly = i, j

    lever_cnt = find(maps, n, m, sx, sy, 'L')
    if lever_cnt == int(1e9):
        return -1

    exit_cnt = find(maps, n, m, lx, ly, 'E')
    if exit_cnt == int(1e9):
        return -1

    return lever_cnt + exit_cnt