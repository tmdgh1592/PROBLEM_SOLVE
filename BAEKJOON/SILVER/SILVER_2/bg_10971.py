import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
min_cost = sys.maxsize


def dfs(start, now, cost):
    global min_cost

    if all(visited) and graph[now][start] != 0:  # 모두 방문했다면
        min_cost = min(min_cost, cost + graph[now][start])  # 최소 비용 비교
        return

    for i in range(n):
        if not visited[i] and graph[now][i] != 0: # 방문하지 않은 곳, 현 위치에서 같은 위치로 이동 X
            visited[i] = True
            dfs(start, i, cost+graph[now][i])
            visited[i] = False


for i in range(n):
    visited = [False] * n
    visited[i] = True
    dfs(i, i, 0)
print(min_cost)
