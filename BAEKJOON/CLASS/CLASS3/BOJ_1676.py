#-*- coding:utf-8 -*-
from math import factorial
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

f = str(factorial(int(input())))
cnt = 0

for i in range(len(f)-1,-1,-1):
    if f[i] == '0': cnt += 1
    else: break
print(cnt)