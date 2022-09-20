#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

for _ in range(int(input())):
    k, n = int(input()), int(input())
    people = [i for i in range(1, n+1)]
    for i in range(1, k+1):
        for j in range(1, n):
            people[j] += people[j-1]
    print(people[-1])