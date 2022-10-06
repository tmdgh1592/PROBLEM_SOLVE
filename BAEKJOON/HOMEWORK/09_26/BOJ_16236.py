#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = []
visited = [[False] * n for _ in range(n)]
opers = [(-1, 0), (0, -1), (1, 0) , (0, 1)]
sx = sy = 0

flag = True
for i in range(n):
    row = list(MIS())
    graph.append(row)
    for j in range(n):
        # 먹을 수 있는게 하나라도 있다면
        if row[j] == 1: flag = False
        if row[j] == 9:
            sx = i; sy = j

# 먹을게 하나도 없으면 0 출력 후 종료
if flag:
    print(0)
    sys.exit()

q = deque([(sx, sy, 0)])
while q:
    x, y, time = q.popleft()



