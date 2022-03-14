import sys

input = sys.stdin.readline
A, B = map(int, input().split())

Q, R = divmod(A, B)

if(A != 0 and R < 0):
    Q += 1
    R -= B

print(f'{Q}\n{R}')
