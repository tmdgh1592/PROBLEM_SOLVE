#-*- coding:utf-8 -*-
import sys
from typing import Counter

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = sorted([int(input().rstrip()) for _ in range(n)])

def find_second_freq(arr):
    counter = Counter(arr)
    most_list = counter.most_common(2)

    return most_list[-(most_list[0][1] == most_list[-1][1])][0]
    
print(int(round(sum(arr)/n, 0)))
print(arr[n//2])
print(find_second_freq(arr))
print(arr[-1] - arr[0])