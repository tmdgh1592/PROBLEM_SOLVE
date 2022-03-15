import sys
import math
input = sys.stdin.readline

arr = list(map(int, (input().split())))
pow_sum = 0
for x in arr:
    pow_sum += x**2

print(pow_sum % 10)