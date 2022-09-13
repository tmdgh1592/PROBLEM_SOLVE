#-*- coding:utf-8 -*-
from collections import deque
from copy import deepcopy
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
count = sys.maxsize
dx, dy = [-1,1,0,0], [0,0,-1,1]
graph = [list(input().rstrip()) for _ in range(n)]


def bfs(eight_graph, temp_count=0):
    global count

    q = deque()
    q.append((0, 0))
    visited = [[False] * 8 for _ in range(8)]

    while q:
        x, y = q.popleft()

        if visited[x][y]:
            continue

        visited[x][y] = True


        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < 8 and 0 <= ny < 8:
                if eight_graph[x][y] == eight_graph[nx][ny]:
                    if eight_graph[x][y] == 'W':
                        eight_graph[nx][ny] = 'B'
                    else:
                        eight_graph[nx][ny] = 'W'
                    temp_count += 1

                if not visited[nx][ny]:
                    q.append((nx, ny))

    count = min(count, temp_count)
    


for i in range(n-7):
    for j in range(m-7):
        new_graph = [row[j:j+8] for row in graph[i:i+8]]

        bfs(deepcopy(new_graph), 0)

        if new_graph[0][0] == 'W':
            new_graph[0][0] = 'B'
        else:
            new_graph[0][0] = 'W'

        bfs(deepcopy(new_graph), 1)

print(count)