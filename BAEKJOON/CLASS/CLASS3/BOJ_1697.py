#-*- coding:utf-8 -*-
from collections import deque
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

start, dest = MIS()
res = sys.maxsize


def f(start, dest):
    visited = [False] * 100001
    q = deque([(start, 0)])
    result = sys.maxsize

    while q:
        now, count = q.popleft()
        
        if not (0 <= now <= 100000): continue
        if visited[now]: continue
        visited[now] = True

        if now == dest:
            result = min(result, count)

        q.append((now+1, count+1))
        q.append((now-1, count+1))
        q.append((now*2, count+1))

    return result

print(f(start, dest))