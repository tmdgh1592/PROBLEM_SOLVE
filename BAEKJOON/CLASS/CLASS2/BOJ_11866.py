#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, k = MIS()
q = [i for i in range(1, n+1)]
i = k-1
arr = []

while q:
    i %= n
    arr.append(q.pop(i))
    i+=(k-1)
    n-=1

print('<', end='')
print(*arr, sep=', ', end ='')
print('>')