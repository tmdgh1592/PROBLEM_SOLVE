#-*- coding:utf-8 -*-
import re
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
cnt = 1
pat = re.compile('6{3,}')

for i in range(666, int(1e9)):
    if (a:=pat.search(str(i))):
        if cnt == n:
            print(i)
            break
        cnt+=1