import sys

input = sys.stdin.readline

mstack = []

n = int(input())

for _ in range(n):
    cmd = input().split()

    if cmd[0] == "push":
        mstack.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if len(mstack) == 0:
            print(-1)
        else:
            print(mstack.pop())
    elif cmd[0] == "size":
        print(len(mstack))
    elif cmd[0] == "empty":
        if len(mstack) == 0:
            print(1)
        else:
            print(0)
    else:
        if len(mstack) == 0:
            print(-1)
        else:
            print(mstack[-1])
