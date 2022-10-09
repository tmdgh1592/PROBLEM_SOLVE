#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

dp = [0] * (101)
dp[0] = dp[1] = dp[2] = dp[3] = 1
dp[4] = dp[5] = 2

for _ in range(int(input())):
    n = int(input())
    
    if n <= 5:
        print(dp[n]); continue
    
    for i in range(6, n + 1):
        dp[i] = dp[i-1] + dp[i-5]
        
    print(dp[n])