#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
graph = [list(map(int, list(input().rstrip()))) for _ in range(n)]

def check(x, y, size):
    init = graph[x][y]
    for i in range(x, x+size):
        for j in range(y, y+size):
            if init != graph[i][j]:
                return False
    return True

def f(x, y, size):
    if size == 1:
        print(graph[x][y], end='')
        return
    
    if check(x, y, size):
        print(graph[x][y], end='')
        return
                
    interval = size // 2

    print('(', end='')
    f(x, y, interval)
    f(x, y+interval, interval)
    f(x+interval, y, interval)
    f(x+interval, y+interval, interval)
    print(')', end='')

f(0, 0, n)