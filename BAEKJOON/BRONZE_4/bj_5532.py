import math

L, A, B, C, D = [int(input()) for _ in range(5)]

korean_q = math.ceil(A / C)
math_q = math.ceil(B / D)

print(L - max(korean_q, math_q))