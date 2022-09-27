#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
graph = []

zero = tomato = 0
temp = deque()
#visited = [[False] * n for _ in range(m)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
required = 0

for i in range(m):
    row = list(MIS())
    graph.append(row)

    for j in range(n):
        if row[j] == 1: # 처음부터 익어 있는 토마토 추가
            tomato+=1
            temp.append((i, j))
            required += 1
            #visited[i][j] = True
        elif row[j] == 0:
            zero += 1
            required += 1

# 토마토가 이미 모두 익어있는 경우
if zero == 0: print(0)
else:
    prev_tomato = len(temp)

    # 현재 익은 토마토가 이전에 익은 토마토 개수와 같은지 확인
    # 같으면 탐색을 그만두고 -1 출력
    # def is_possible():
    #     global prev_tomato

    #     cnt = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if graph[i][j] == 1:
    #                 cnt += 1
    #     #print(prev_tomato, cnt)
    #     if cnt == prev_tomato and cnt != required:
    #         return True

    #     prev_tomato = cnt
    #     return False


    def bfs():
        global tomato
        q = deque()
        day = -1 # 처음 시작값은 빼고 계산해야하기 때문에 -1부터
        
        while temp:
            day += 1
            q.extend(temp); temp.clear()

            while q:
                x, y = q.popleft()
                
                for i in range(4):
                    nx, ny = x+dx[i], y+dy[i]
                    if 0 <= nx < m and 0 <= ny < n: # 범위 체크
                        if graph[nx][ny] == 0: # 토마토가 익지 않았고 방문하지 않은경우
                            graph[nx][ny] = 1
                            tomato += 1
                            temp.append((nx, ny))
            
            if len(temp) == 0 and required != tomato: return -1

        return day
            
    print(bfs())