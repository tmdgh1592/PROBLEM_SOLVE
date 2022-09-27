#-*- coding:utf-8 -*-
import sys
sys.setrecursionlimit(int(1e6))
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

n = int(input())
memo = [0] * (1001)
memo[1], memo[2] = 1, 2

def f(i):
    if memo[i] != 0:
        return memo[i] % 10007
    memo[i] = (f(i-1) + f(i-2)) % 10007
    return memo[i]

print(f(n))