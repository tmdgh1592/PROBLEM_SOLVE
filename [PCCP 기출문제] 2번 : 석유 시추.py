from collections import deque

dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def bfs(land, n, m, sx, sy, oil_id):
    q = deque([(sx, sy)])
    land[sx][sy] = oil_id
    cnt = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m): continue
            if land[nx][ny] != 1: continue
            q.append((nx, ny))
            land[nx][ny] = oil_id
            cnt += 1
    return cnt


def solution(land):
    row = len(land)
    col = len(land[0])
    oil_id = 2
    oils = {0: 0}

    for c in range(col):
        for r in range(row):
            if land[r][c] == 1:
                oils[oil_id] = bfs(land, row, col, r, c, oil_id)
                oil_id += 1

    answer = -1

    for c in range(col):
        oil_types = set([land[r][c] for r in range(row)])
        cnt = 0
        for type in oil_types:
            cnt += oils[type]
        answer = max(answer, cnt)

    return answer
