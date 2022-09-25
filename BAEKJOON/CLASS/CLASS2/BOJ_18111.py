#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, inventory = MIS()
arr = [list(MIS()) for _ in range(n)]
min_cost = sys.maxsize
ans_height = 0

for height in range(257):
    need = get = 0

    for i in range(n):
        for j in range(m):
            if height <= arr[i][j]: get += (arr[i][j] - height)
            else: need += (height - arr[i][j])
    
    if get + inventory >= need:
        now_cost = get * 2 + need
        if now_cost <= min_cost:
            min_cost = now_cost
            ans_height = height

print(min_cost, ans_height)