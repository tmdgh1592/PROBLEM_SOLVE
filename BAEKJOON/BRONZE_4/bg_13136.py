import math

R, C, N = map(int, input().split())

A = math.ceil(R/N)
B = math.ceil(C/N)

print(A*B)
