#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

target = int(input()); input()
broken = list(MIS())

result = abs(100 - target)

for nums in range(1000001):
    for num in str(nums):
        if int(num) in broken: break
    else:
        result = min(result, len(str(nums)) + abs(nums - target))

print(result)