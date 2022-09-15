#-*- coding:utf-8 -*-
from math import gcd, lcm
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

a, b = MIS()
print(gcd(a,b), lcm(a,b))