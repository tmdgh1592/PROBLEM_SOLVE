import copy
import sys
sys.setrecursionlimit(10 ** 8)


n = int(input())
org_graph = []

for _ in range(n):
    org_graph.append(list(map(int, input().split())))

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(graph, x, y, now_height):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] < now_height:
        return False

    # 방문처리
    graph[x][y] = 0

    for i in range(4):
        dfs(graph, x+dx[i], y+dy[i], now_height)

    return True

max_result = 0
max_height = 0
for h in range(10):
    result = 0
    for i in range(n):
        for j in range(n):
            if dfs(copy.deepcopy(org_graph), i, j, h):
                result += 1

    if max_result < result:
        max_result = result
        max_height = h

    

print(max_height)