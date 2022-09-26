#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(MIS()) for _ in range(n)]
counts = {-1:0, 0:0, 1:0}

def dfs(sx, sy, size):
    if size == 1:
        counts[arr[sx][sy]] += 1
        return
    if size == 0: return
    
    init_state = arr[sx][sy]

    for i in range(sx, sx + size):
        for j in range(sy, sy + size):
            if init_state != arr[i][j] and size // 3 != 0: # 색이 다르면 9개씩 재귀호출
                for a in range(sx, sx+size, size // 3):
                    for b in range(sy, sy+size, size // 3):
                        dfs(a, b, size // 3)
                return

    counts[arr[sx][sy]] += 1


dfs(0, 0, n)
print(*counts.values(), sep='\n')