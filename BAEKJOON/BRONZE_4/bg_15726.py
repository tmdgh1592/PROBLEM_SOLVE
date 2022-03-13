import math

A, B, C = map(int, input().split())
print(math.floor(max(A*B/C, A/B*C)))
