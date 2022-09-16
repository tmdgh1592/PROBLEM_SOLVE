#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

sort_key = lambda x:(x[1], x[0])

n = int(input())
arr = []
for i in range(n):
    data = input().rstrip().rsplit()
    arr.append((i, int(data[0]), data[1]))
[print(info[1], info[2]) for info in sorted(arr, key=sort_key)]