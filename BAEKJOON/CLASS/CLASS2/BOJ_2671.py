#-*- coding:utf-8 -*-
import re
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

# (100~1~|01)~
word = input().rstrip()
print('SUBMARINE' if re.fullmatch('((100+1+)|01)+', word) else 'NOISE')