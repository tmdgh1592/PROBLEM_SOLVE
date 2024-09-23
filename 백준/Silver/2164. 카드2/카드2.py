from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
q = deque([i + 1 for i in range(n)])

while len(q) > 1:
    q.popleft()
    if len(q) > 1:
        q.append(q.popleft())

print(q[0])