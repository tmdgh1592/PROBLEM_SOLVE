import sys
input = sys.stdin.readline
arr = 0b00000000000000000000

for _ in range(int(input())):
    inst = input().split()
    n = 0
    if len(inst) == 2:
        n = int(inst[1]) - 1
    inst = inst[0]

    if inst == 'add':
        arr = arr | (1 << n)
    if inst == 'remove':
        arr = arr & ~(1 << n)
    if inst == 'check':
        if arr & (1 << n) > 0:
            print(1)
        else:
            print(0)
    if inst == 'toggle':
        arr = arr ^ (1 << n)
    if inst == 'all':
        arr = 0b11111111111111111111
    if inst == 'empty':
        arr = 0b00000000000000000000
