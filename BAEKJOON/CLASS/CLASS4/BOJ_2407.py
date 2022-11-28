#-*- coding:utf-8 -*-
from math import factorial
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
parent = factorial(n)
child = factorial(n - m) * factorial(m)
print(parent // child)