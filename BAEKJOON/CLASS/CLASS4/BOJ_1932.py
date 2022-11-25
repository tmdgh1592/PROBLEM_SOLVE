#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
data = [list(MIS()) for _ in range(n)]
cache = [[-1] * n for _ in range(n)] # 깊이 i에서 최대 값

def f(depth, left):
    if depth == n - 1:
        return data[depth][left]
    if cache[depth][left] != -1:
        return cache[depth][left]
    
    cache[depth][left] = -float('inf')
    cache[depth][left] = max(cache[depth][left], f(depth + 1, left) + data[depth][left], f(depth + 1, left + 1) + data[depth][left])
    return cache[depth][left]

print(f(0, 0))