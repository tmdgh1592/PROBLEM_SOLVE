#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = sorted([int(input()) for _ in range(n)], reverse=True)

res = 0
for i, tip in enumerate(arr):
    real_tip = tip - i
    if real_tip > 0:
        res += real_tip
        
print(res)