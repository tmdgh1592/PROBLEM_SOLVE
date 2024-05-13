import heapq

dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]  # 우 하 상 좌


def solution(board):
    n = len(board)
    answer = int(1e9)
    visited = [[[False] * 3 for _ in range(n)] for _ in range(n)]
    q = [(0, 0, 0, 2)]  # 비용, x좌표, y좌표, 직전 방향

    while q:
        cost, x, y, d = heapq.heappop(q)
        visited[x][y][d] = True

        if x == n - 1 and y == n - 1:
            answer = min(answer, cost)
            continue

        for i in range(4):
            nx, ny = x + dirs[i][0], y + dirs[i][1]
            is_horizontal = int(i == 0 or i == 3)  # 좌우인가

            if not (0 <= nx < n and 0 <= ny < n): continue
            if visited[nx][ny][is_horizontal]: continue
            if board[nx][ny]: continue

            if (d == 0 and is_horizontal) or (d == 1 and not is_horizontal):
                heapq.heappush(q, ((cost + 600, nx, ny, is_horizontal)))
            else:
                heapq.heappush(q, ((cost + 100, nx, ny, is_horizontal)))
    return answer
