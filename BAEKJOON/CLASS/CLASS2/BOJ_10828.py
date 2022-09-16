#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

stack = []

def process1(command):
    if command == 'pop':
        if is_empty(): print(-1)
        else: print(stack.pop())
    elif command == 'size':
        print(len(stack))
    elif command == 'empty':
        if is_empty(): print(1)
        else: print(0)
    elif command == 'top':
        if is_empty(): print(-1)
        else: print(stack[-1])

def process2(command, num):
    if command == 'push':
        stack.append(num)

def is_empty():
    return len(stack) == 0

for _ in range(int(input())):
    x = input().rstrip().split()
    if len(x) == 1:
        command = x[0]
        process1(command)
    else:
        command, num = x
        process2(command, num)