# -*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

round = 1
while(n := int(input())):
    names = dict()
    nums = [0] * (n + 1)
    for i in range(1, n + 1):
        names[i] = input().rstrip()
    for _ in range(2 * n - 1):
        idx, name = input().rstrip().split()
        nums[int(idx)] += 1

    print(f"{round} {names[nums.index(1)]}")
    round += 1
