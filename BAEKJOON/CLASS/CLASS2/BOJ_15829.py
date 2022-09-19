#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
r, m = 31, 1234567891
input()
result = 0
for i, x in enumerate(input().rstrip()):
    result += ((ord(x)-96) * (r ** i))
print(result % m)