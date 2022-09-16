#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

q = deque()


def process1(command):
    if command == 'pop_front':
        if is_empty():
            print(-1)
        else:
            print(q.popleft())
    elif command == 'pop_back':
        if is_empty():
            print(-1)
        else:
            print(q.pop())
    elif command == 'size':
        print(len(q))
    elif command == 'empty':
        if is_empty():
            print(1)
        else:
            print(0)
    elif command == 'front':
        if is_empty():
            print(-1)
        else:
            print(q[0])
    elif command == 'back':
        if is_empty():
            print(-1)
        else:
            print(q[-1])

def process2(command, num):
    if command == 'push_front':
        q.appendleft(num)
    elif command == 'push_back':
        q.append(num)

def is_empty():
    return len(q) == 0

for _ in range(int(input())):
    x = input().rstrip().split()
    if len(x) == 1:
        command = x[0]
        process1(command)
    else:
        command, num = x
        process2(command, num)
        