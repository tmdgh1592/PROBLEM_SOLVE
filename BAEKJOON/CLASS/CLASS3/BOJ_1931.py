#-*- coding:utf-8 -*-
import sys

input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

times = []
for _ in range(int(input())):
    times.append(list(MIS()))
times.sort(key=lambda x: (x[1], x[0]))

count = 1
last_end = times[0][1]

for start, end in times[1:]:
    if start >= last_end:
        count += 1
        last_end = end

print(count)