#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

while True:
    a, b, c = sorted(MIS())
    if a==0 and b==0 and c==0:
        break
    if c ** 2 == a**2+b**2:
        print('right')
    else:
        print('wrong')