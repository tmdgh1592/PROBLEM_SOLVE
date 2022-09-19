#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())
n = int(input())
arr = [int(input()) for _ in range(n)]
print(*sorted(arr), sep='\n')