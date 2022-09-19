#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = [tuple(MIS()) for _ in range(n)]
for x in sorted(arr, key=lambda x:(x[1],x[0])):
    print(*x)