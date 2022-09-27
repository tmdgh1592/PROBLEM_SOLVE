#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def bfs(tomato):
    day = -1
    
    while tomato_locs:
        q = deque(tomato_locs)
        tomato_locs.clear()
        day += 1

        while q:
            x, y, z = q.popleft()

            for i in range(6):
                nx, ny, nz = x+dx[i], y+dy[i], z+dz[i]

                if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h:
                    if graph[nz][nx][ny] == 0:
                        graph[nz][nx][ny] = 1
                        tomato += 1
                        tomato_locs.append((nx, ny, nz))

        if len(tomato_locs) == 0 and required != tomato: return -1
    return day
    

n, m, h = MIS()
tomato_locs = deque()
required = tomato = zero = 0
graph = [[] for _ in range(h)]


for z in range(h):
    for x in range(m):
        row = list(MIS())
        graph[z].append(row)
        for y in range(n):
            if row[y] == 1:
                tomato_locs.append((x, y, z))
                required += 1
                tomato += 1
            elif row[y] == 0:
                required += 1
                zero += 1

if zero == 0:
    print(0)
    sys.exit()

dx, dy, dz = [-1,1,0,0,0,0], [0,0,-1,1,0,0], [0,0,0,0,-1,1]
print(bfs(tomato))