#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def flip(a, b):
    for i in range(a+1):
        for j in range(b+1):
            arr[i][j] ^= 1

n, m = MIS()
arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]
res = 0

for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if arr[i][j]:
            res += 1
            flip(i, j)

print(res)