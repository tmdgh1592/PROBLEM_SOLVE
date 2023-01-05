#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
arr = [list(MIS()) for _ in range(n)]
result = sys.maxsize


def calc(lst):
    #return sum([arr[i][j] for j in lst for i in lst])
    total = 0
    for i in lst:
        for j in lst:
            if i == j: continue
            total += arr[i][j]
    return total

for bits in range(1 << n):
    cnt = 0
    zeros, ones = [], [] # 팀을 0 또는 1 비트로 나눔

    for i in range(n):
        if bits & 1 << i:
            ones.append(i)
            cnt += 1
        else: zeros.append(i)

    # 딱 절반으로 나누어지지 않은 경우 스킵
    if cnt != (n // 2): continue

    result = min(result, abs(calc(zeros) - calc(ones)))

print(result)