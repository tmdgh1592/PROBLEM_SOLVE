from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])
ans = []

while q:
    for _ in range(k - 1):
        x = q.popleft()
        q.append(x)
    ans.append(str(q.popleft()))

print("<", end="")
print(', '.join(ans), end="")
print(">")
