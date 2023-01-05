#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e9))

n, c, k = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[False] * c for _ in range(n)]
res = 0
opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < c

def dfs(x, y, count):
    global res

    if graph[x][y] == 'T': return
    if count == k and x == 0 and y == c-1:
        res += 1
        return

    for oper in opers:
        nx, ny = x+oper[0], y+oper[1]
        if in_range(nx, ny) and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, count + 1)
            visited[nx][ny] = False

visited[n-1][0] = True
dfs(n-1, 0, 1)
print(res)