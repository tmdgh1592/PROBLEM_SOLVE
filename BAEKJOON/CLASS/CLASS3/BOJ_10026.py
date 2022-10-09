#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def bfs(sx, sy, is_weakness):
    q = deque([(sx, sy)])
    color = graph[sx][sy]
    visited[sx][sy] = True

    while q:
        x, y = q.popleft()

        for oper in opers:
            nx, ny = x + oper[0], y + oper[1]
            if in_range(nx, ny) and not visited[nx][ny]:
                if is_weakness:
                    if color == 'R' or color == 'G':
                        if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                            q.append((nx, ny))
                            visited[nx][ny] = True
                    else: # blue
                        if graph[nx][ny] == color:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                else:
                    if graph[nx][ny] == color:
                        q.append((nx, ny))
                        visited[nx][ny] = True
                

for is_weakness in range(2):
    visited = [[False] * n for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j, is_weakness)
                res += 1
    
    print(res, end=' ')