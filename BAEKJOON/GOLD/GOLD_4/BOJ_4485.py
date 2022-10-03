#-*- coding:utf-8 -*-
import heapq
import sys
sys.setrecursionlimit(int(1e9))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
INF = int(1e9)

opers = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dijkstra():
    q = [(graph[0][0], 0, 0)]
    distance[0][0] = graph[0][0]
    
    while q:
        cost, x, y = heapq.heappop(q)
        if cost > distance[x][y]: continue

        for oper in opers:
            nx, ny = x + oper[0], y + oper[1]
            if 0 <= nx < n and 0 <= ny < n:
                next_cost = cost + graph[nx][ny]
                if next_cost < distance[nx][ny]:
                    distance[nx][ny] = next_cost
                    heapq.heappush(q, (next_cost, nx, ny))
    
    return distance[n-1][n-1]
    

tc = 1
while((n:=int(input())) != 0):
    graph = [list(MIS()) for _ in range(n)]
    distance = [[INF] * (n) for _ in range(n)]
    print(f'Problem {tc}: {dijkstra()}')
    tc += 1