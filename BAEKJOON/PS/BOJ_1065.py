#-*- coding:utf-8 -*-
import sys
input = sys.stdin.readline

n = int(input())
answer = 0
for number in range(1, n + 1):
    if number < 100:
        answer += 1
        continue
    
    diff = 0
    for i in range(len(str(number)) - 1):
        new_diff = int(str(number)[i]) - int(str(number)[i + 1])
        if diff != new_diff and i != 0: break
        diff = new_diff
    else:
        answer += 1
print(answer)