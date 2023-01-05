#-*- coding:utf-8 -*-
from collections import deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def f(start):
    count = 0
    q = deque([start])

    while q:
        now = q.popleft()
        visited[now] = True

        for next in graph[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                count += 1

    return count

n, m = MIS()
graph = [[] for _ in range(n + 1)]
max_count = -sys.maxsize
res = []

for _ in range(m):
    a, b = MIS()
    graph[b].append(a)

for x in range(1, n+1):
    visited = [False] * (n + 1)
    visited[x] = True
    count = f(x)

    if count == max_count:
        res.append(x)
    elif count > max_count:
        max_count = count
        res = [x]

print(*res)