import copy
import sys
sys.setrecursionlimit(int(1e6))


n = int(input())
org_graph = []

for _ in range(n):
    org_graph.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] < n:
        return False

    # 방문처리
    graph[x][y] = 0

    for i in range(4):
        dfs(graph, x+dx[i], y+dy[i])

    return True

result = 0
for i in range(n):
    for j in range(n):
        if dfs(org_graph, i, j):
            result += 1

    

print(result)