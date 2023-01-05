import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:
        return False

    if graph[x][y] == 1:  # 방문하지 않은 위치 중에서 방문할 수 있는 위치라면
        graph[x][y] = 0  # 방문처리(재방문X)
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            dfs(nx, ny)

        return True

    return False


for _ in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * (m) for _ in range(n)]
    count = 0

    for _ in range(k):
        X, Y = map(int, input().split())
        graph[Y][X] = 1

    for i in range(n):
        for j in range(m):
            if dfs(i, j):
                count += 1

    print(count)
