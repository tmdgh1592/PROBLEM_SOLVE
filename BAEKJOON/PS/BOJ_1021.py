#-*- coding:utf-8 -*-
from collections import deque
import sys
input = sys.stdin.readline

left_stack = deque(input().rstrip())
right_stack = deque()

n = int(input())
for _ in range(n):
    query = input().rstrip().split()
    if query[0] == 'L':
        if left_stack:
            right_stack.appendleft(left_stack.pop())
    elif query[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.popleft())
    elif query[0] == 'B':
        if left_stack:
            left_stack.pop()
    else:
        val = query[1]
        left_stack.append(val)

print(*(left_stack + right_stack), sep='')