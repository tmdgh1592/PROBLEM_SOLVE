#-*- coding:utf-8 -*-
from math import ceil
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

a,b,v = MIS()
print(1 + ceil((v-a) / (a-b)))