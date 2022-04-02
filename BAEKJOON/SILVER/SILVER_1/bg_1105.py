import sys
input = sys.stdin.readline

L, R = map(int, input().split())
count = int(1e9)

while L <= R and count != 0:
    str_l = str(L).count('8')
    count = min(count, str_l)
    L += 1

print(count)
