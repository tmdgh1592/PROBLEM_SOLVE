from collections import deque
import sys

input = sys.stdin.readline


def is_vps(data):
    stack = deque()

    for x in data:
        if x == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return False
            if stack[-1] != '(':
                return False
            stack.pop()

    return len(stack) == 0


n = int(input())

for _ in range(n):
    if is_vps(input().strip()):
        print("YES")
    else:
        print("NO")
