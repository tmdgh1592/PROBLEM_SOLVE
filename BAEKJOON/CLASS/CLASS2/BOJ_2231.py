#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())

for x in range(1, n+1):
    total = x + sum(list(map(int, str(x))))
    if total == n:
        print(x)
        break

    if x == n:
        print(0)