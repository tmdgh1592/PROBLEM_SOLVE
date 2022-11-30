# -*- coding:utf-8 -*-
from collections import deque
from copy import deepcopy
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
def MIS(): return map(int, input().rstrip().split())


r, c = MIS()
graph = []
virus = []

for i in range(r):
    graph.append(list(MIS()))
    for j in range(c):
        if graph[i][j] == 2:
            virus.append((i, j))


def in_range(x, y): return 0 <= x < r and 0 <= y < c


def bfs():
    q = deque(virus)
    c_graph = deepcopy(graph)
    opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    visited = [[False] * c for _ in range(r)]

    while q:
        x, y = q.popleft()
        if c_graph[x][y] == 0:
            c_graph[x][y] = 2

        for oper in opers:
            nx, ny = x+oper[0], y+oper[1]
            if not in_range(nx, ny):
                continue
            if visited[nx][ny]:
                continue
            if c_graph[nx][ny] != 0:
                continue

            visited[nx][ny] = True
            q.append((nx, ny))

    count_0 = 0
    for row in c_graph:
        count_0 += row.count(0)
    return count_0


def f(cnt):
    if cnt == 3:
        return bfs()

    res = -1
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 0:
                graph[i][j] = 1
                res = max(res, f(cnt + 1))
                graph[i][j] = 0

    return res


print(f(0))
