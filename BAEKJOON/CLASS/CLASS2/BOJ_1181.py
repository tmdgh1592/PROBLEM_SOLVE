#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = list(set([input().rstrip() for _ in range(n)]))
arr.sort(key=lambda x:(len(x), x))
print(*arr, sep='\n')