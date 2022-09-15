#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

q = deque([x for x in range(1, int(input())+1)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q[0])