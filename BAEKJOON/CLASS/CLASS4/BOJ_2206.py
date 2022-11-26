#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def in_range(x, y):
    return 0 <= x < r and 0 <= y < c

r, c = MIS()
graph = [list(map(int, list(input().rstrip()))) for _ in range(r)]
opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dist = [[[0] * c for _ in range(r)] for _ in range(2)]
q = deque([(0, 0, 0)])
dist[0][0][0] = dist[1][0][0] = 1

while q:
    x, y, broken = q.popleft()
    if x == r-1 and y == c-1:
        print(dist[broken][x][y])
        break
    
    for oper in opers:
        nx = x + oper[0]
        ny = y + oper[1]

        if not in_range(nx, ny): continue
        if graph[nx][ny] == 1 and broken == 1: continue
        
        # 벽이 있지만 아직 부수지 않았다면 부수고 이동
        if graph[nx][ny] == 1 and broken == 0:
            if dist[1][nx][ny] != 0: continue
            dist[1][nx][ny] = dist[0][x][y] + 1
            q.append((nx, ny, 1))
        # 벽이 없는 경우 그대로 이동
        if graph[nx][ny] == 0 and dist[broken][nx][ny] == 0:
            dist[broken][nx][ny] = dist[broken][x][y] + 1
            q.append((nx, ny, broken))
else:
    print(-1)