#-*- coding:utf-8 -*-
from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
radd = defaultdict(int)
snakes = defaultdict(int)

def init():
    for _ in range(n):
        x, y = MIS()
        radd[x] = y
    for _ in range(m):
        x, y = MIS()
        snakes[x] = y


init()
q = deque([(1, 0)])
res = sys.maxsize
visited = [False] * (101)
visited[1] = True

while q:
    now, count = q.popleft()
    if now >= 100:
        res = min(res, count)

    for move in range(1, 7):
        next = now + move
        if next > 100 or visited[next]: continue
        if radd[now + move]: next = radd[now + move]
        if snakes[now + move]: next = snakes[now + move]
        if not visited[next]:
            visited[next] = True
            q.append((next, count + 1))

print(res)