from collections import deque


def solution(board):
    answer = int(1e9)
    n = len(board)
    m = len(board[0])

    q = deque()
    visited = [[False] * m for _ in range(n)]
    dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                q.append((i, j, 0))

    while q:
        x, y, move = q.popleft()

        if board[x][y] == 'G':
            answer = min(answer, move)

        for i in range(4):
            nx, ny = x, y
            while 0 <= nx < n and 0 <= ny < m:
                print(board[nx + dx[i]][ny + dy[i]])
                if board[nx + dx[i]][ny + dy[i]] == 'D':
                    print(board[nx + dx[i]][ny + dy[i]])
                    break
                nx += dx[i]
                ny += dy[i]
            if visited[nx][ny]: continue

            q.append((nx, ny, move + 1))
            visited[nx][ny] = True

    return answer


solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."])