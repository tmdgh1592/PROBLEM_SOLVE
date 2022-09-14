#-*- coding:utf-8 -*-
from collections import deque
import re
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = deque([int(input()) for _ in range(n)])
stack = []
result = [] # +, - 를 저장할 공간
flag = False

for i in range(1, n+1):
    stack.append(i)
    result.append('+')
    
    cur = i
    while arr[0] == cur:
        stack.pop()
        arr.popleft()
        result.append('-')

        if stack:
            cur = stack[-1]
        else:
            break

if stack and stack[-1] != arr[0]:
    print('NO')
else:
    print(*result, sep='\n')