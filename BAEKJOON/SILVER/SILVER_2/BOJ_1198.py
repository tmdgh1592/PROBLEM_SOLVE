#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def trinagle(a, d, b, e, c, f):
    first = a * e + b * f + c * d
    second = d * b + e * c + f * a
    return abs((first - second) / 2)

def f(dots, cnt):
    if cnt == 3:
        return trinagle(*dots[0], *dots[1], *dots[2])
    
    res = -float('inf')
    for i in range(n):
        if used[i]: continue
        used[i] = True; dots.append(data[i])
        res = max(res, f(dots, cnt + 1))
        used[i] = False; dots.pop()
        
    return res
        

n = int(input())
data = [tuple(MIS()) for _ in range(n)]
used = [False] * n
print(f([], 0))