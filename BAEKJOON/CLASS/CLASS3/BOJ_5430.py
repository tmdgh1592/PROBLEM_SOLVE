#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    commands = input().rstrip()
    n = int(input())
    arr = input().rstrip()[1:-1].split(',')
    if not arr[0]:
        if 'D' in commands: print('error')
        else: print('[]')
        continue

    queue1 = deque(map(int, arr))
    queue2 = deque(map(int, arr))
    queue2.reverse()
    length = len(arr)
    reversed = False

    for cmd in commands:
        if cmd == 'R':
            reversed = not reversed
        else:            
            if length > 0:
                if not reversed:
                    queue1.popleft()
                    queue2.pop()
                else:
                    queue2.popleft()
                    queue1.pop()
                length -= 1
            else:
                print('error')
                break
    else:
        if not reversed:
            print('[' + ','.join(map(str, queue1)) + ']')
        else:
            print('[' + ','.join(map(str, queue2)) + ']')