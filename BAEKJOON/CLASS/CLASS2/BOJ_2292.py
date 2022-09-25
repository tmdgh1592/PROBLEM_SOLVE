#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
i = cnt = 1

while n > cnt:
    cnt += (6 * i)
    i+=1
print(i)