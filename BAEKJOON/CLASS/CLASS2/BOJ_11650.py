#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

incs = lambda x:(x[0], x[1])

n = int(input())
arr = [tuple(MIS()) for _ in range(n)]

for x in sorted(arr, key=incs):
    print(x[0], x[1])