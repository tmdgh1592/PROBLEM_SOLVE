from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def solution(board):
    sx, sy = 0, 0
    gx, gy = 0, 0
    obstacles = set()

    def in_range(x, y):
        n, m = len(board), len(board[0])
        return (0 <= x < n) and (0 <= y < m)

    def is_obstacle(x, y):
        return (x, y) in obstacles

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                sx, sy = i, j
            elif board[i][j] == 'G':
                gx, gy = i, j
            elif board[i][j] == 'D':
                obstacles.add((i, j))

    visited = [[False] * len(board[0]) for _ in range(len(board))]
    q = deque([(sx, sy, 0)])
    visited[sx][sy] = True

    while q:
        x, y, cost = q.popleft()
        if x == gx and y == gy: return cost

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            while True:
                if not in_range(nx, ny): break
                if is_obstacle(nx, ny): break
                nx, ny = nx + dx[i], ny + dy[i]

            px, py = nx - dx[i], ny - dy[i]
            if visited[px][py]: continue

            q.append((px, py, cost + 1))
            visited[px][py] = True

    return -1