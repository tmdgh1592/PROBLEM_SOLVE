#-*- coding:utf-8 -*-
import math
import sys
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, atk = MIS()
rounds = [list(MIS()) for _ in range(n)]

def possible(curAtk, maxHp):
    curHp = maxHp
    for t, a, h in rounds:
        if t == 1:
            curHp -= (math.ceil(h / curAtk) - 1) * a
            if curHp <= 0: return False
        else:
            curAtk += a
            curHp = min(curHp + h, maxHp)
    return True
            

left = 1
right = int(1e18)
while left <= right:
    mid = (left + right) // 2
    if possible(atk, mid):
        right = mid - 1
    else:
        left = mid + 1
        
print(left)