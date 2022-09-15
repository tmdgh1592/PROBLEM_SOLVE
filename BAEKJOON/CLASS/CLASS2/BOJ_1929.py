#-*- coding:utf-8 -*-
from math import sqrt
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
prime = [True for _ in range(m+1)]
prime[1] = False

# 에라토스테네스의 체
for x in range(2, int(sqrt(m)) + 1):
    if prime[x]:
        i = 2
        while x*i <= m:
            prime[x*i] = False
            i += 1

for x in range(n, m+1):
    if prime[x]: print(x)