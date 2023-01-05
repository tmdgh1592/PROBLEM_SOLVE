import copy
import sys
sys.setrecursionlimit(10 ** 6)
visited = -1


def dfs(graph, x, y, nh):
    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] >= nh:
        # 방문처리
        graph[x][y] = visited

        for i in range(4):
            dfs(graph, x+dx[i], y+dy[i], nh)

        return True
    return False


n = int(input())
org_graph = []  # N x N 기둥 그래프
hh = -1  # 기둥의 최대 높이

for _ in range(n):
    h_arr = list(map(int, input().split()))
    hh = max([hh]+h_arr)  # 기둥 최대 높이 갱신
    org_graph.append(h_arr)

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


max_result = 0
max_height = 0

for h in range(hh+1):
    result = 0
    graph = copy.deepcopy(org_graph)
    for i in range(n):
        for j in range(n):
            if dfs(graph, i, j, h):
                result += 1

    if max_result < result:
        max_result = result
        max_height = h

print(max_result)
