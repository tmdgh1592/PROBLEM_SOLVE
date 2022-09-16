#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    h, w, n = MIS()
    floor, ho = 0, 0
    
    if n % h == 0:
        floor = h * 100
        ho = n // h
    else:
        ho = (n % h) * 100
        floor = n // h + 1

    print(floor+ho)