from collections import deque
import sys

input = sys.stdin.readline

q = deque()


def push(x):
    q.append(x)


def pop():
    if size() == 0:
        print(-1)
    else:
        print(q.popleft())


def size(isPrint=False):
    if isPrint:
        print(len(q))

    return len(q)


def empty():
    if size() == 0:
        print(1)
    else:
        print(0)


def front():
    if size() == 0:
        print(-1)
    else:
        print(q[0])


def back():
    if size() == 0:
        print(-1)
    else:
        print(q[-1])


n = int(input())
for _ in range(n):
    i = input().split()

    if i[0] != 'push':
        cmd = i[0]
        if cmd == 'pop':
            pop()
        elif cmd == 'size':
            size(True)
        elif cmd == 'empty':
            empty()
        elif cmd == 'front':
            front()
        elif cmd == 'back':
            back()
    else:
        push(int(i[1]))
