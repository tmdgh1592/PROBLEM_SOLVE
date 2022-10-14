#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
graph = [list(input().rstrip()) for _ in range(n)]
answer = 1

for size in range(2, min(n, m) + 1):
    size -= 1
    for i in range(n - size):
        for j in range(m - size):
            if graph[i][j] == graph[i+size][j] == graph[i][j+size] == graph[i+size][j+size]:
                answer = (size+1) ** 2

print(answer)