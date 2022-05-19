import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, list(input().rstrip().replace("H", "0"))))
         for _ in range(n)]

max_count = -1
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
INF = int(1e9)
visited = [[False] * m for _ in range(n)]
visited[0][0] = True
dp = [[0]*m for _ in range(n)]


def dfs(x, y, count):
    global max_count

    move = graph[x][y]  # 이동거리
    max_count = max(max_count, count)

    for i in range(4):
        nx = x + dx[i]*move
        ny = y + dy[i]*move

        if 0 <= nx < n and 0 <= ny < m:  # 주어진 범위이고
            if graph[nx][ny] != 0:  # 구멍이 아니라면
                if count+1 > dp[nx][ny]:
                    if visited[nx][ny]:  # 재방문 한다면 사이클 발생!!
                        print(-1)
                        exit(0)

                    dp[nx][ny] = count + 1  # 다음 방문할 곳 count 갱신
                    visited[nx][ny] = True
                    dfs(nx, ny, count+1)
                    visited[nx][ny] = False


dfs(0, 0, 0)
print(max_count+1)
