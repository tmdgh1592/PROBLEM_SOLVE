#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
    
for _ in range(int(input())):
    n = int(input())
    data = [list(MIS()) for _ in range(2)]
    
    if n >= 2:
        data[0][1] += data[1][0]
        data[1][1] += data[0][0]
    
    for i in range(2, n):
            data[0][i] += max(data[1][i-1], data[1][i-2], data[0][i-2])
            data[1][i] += max(data[0][i-1], data[0][i-2], data[1][i-2])
            
    print(max(data[0][n-1], data[1][n-1]))