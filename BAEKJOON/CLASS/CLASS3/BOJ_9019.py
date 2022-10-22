#-*- coding:utf-8 -*-
from collections import defaultdict, deque
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def oper_d(n):
    return (n * 2) % 10000

def oper_s(n):
    if n == 0: return 9999
    return n - 1

def oper_l(n):
    front = n // 1000
    back = n % 1000
    return back * 10 + front

def oper_r(n):
    front = n // 10
    back = n % 10
    return back * 1000 + front

def go(src, dest):
    visited = defaultdict(bool)
    q = deque([(src, '')])
    visited[src] = True

    while q:
        now, cmd = q.popleft()
        if now == dest:
            print(cmd)
            return
    
        next = oper_d(now)
        if not visited[next]:
            visited[next] = True
            q.append((next, cmd+'D'))

        next = oper_s(now)
        if not visited[next]:
            visited[next] = True
            q.append((next, cmd+'S'))

        next = oper_l(now)
        if not visited[next]:
            visited[next] = True
            q.append((next, cmd+'L'))

        next = oper_r(now)
        if not visited[next]:
            visited[next] = True
            q.append((next, cmd+'R'))


for _ in range(int(input())):
    a, b = MIS()
    go(a, b)