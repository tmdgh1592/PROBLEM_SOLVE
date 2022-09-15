#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())


for _ in range(n):
    arr = list(input().rstrip())
    stack = []
    
    for x in arr:
        if x == '(':
            stack.append(x)
        else: # )
            if stack:
                stack.pop()
            else:
                print('NO')
                break
    else:
        if stack:
            print('NO')
        else:
            print('YES')