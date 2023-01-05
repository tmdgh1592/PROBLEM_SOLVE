#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

graph = [list(input().rstrip()) for _ in range(8)]
res = 0
for i in range(8):
    if i % 2 == 0: start = 0
    else: start = 1
    
    for j in range(start, 8, 2):
        if graph[i][j] == 'F':
            res += 1

print(res)