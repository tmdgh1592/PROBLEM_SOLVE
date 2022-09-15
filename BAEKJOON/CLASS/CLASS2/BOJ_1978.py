#-*- coding:utf-8 -*-
from math import sqrt
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

cnt = 0
input()


def is_prime(value):
    if value == 1:
        return False

    for i in range(2, int(sqrt(value)) + 1):
        if value % i == 0:
            return False
    return True


for x in list(MIS()):
    if is_prime(x):
        cnt += 1

print(cnt)