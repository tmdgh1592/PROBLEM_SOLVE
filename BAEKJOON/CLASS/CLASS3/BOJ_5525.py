#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = [int(input()) for _ in range(2)]

arr = list(input().rstrip())
res = count = 0
i = 1

while i < m-1:
    if arr[i-1] == 'I' and arr[i] == 'O' and arr[i+1] == 'I':
        count += 1
        if count == n:
            res += 1
            count -= 1
        i += 1
    else:
        count = 0
    i += 1

print(res)