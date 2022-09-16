#-*- coding:utf-8 -*-
from math import factorial
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


n, k = MIS()
print(int(factorial(n) / (factorial(n-k) * factorial(k))))