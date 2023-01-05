#-*- coding:utf-8 -*-
import sys
from typing import Counter
input = sys.stdin.readline

n = int(input())
arr = [input().rstrip() for _ in range(n)]
best_seller = Counter(arr).most_common()

res, prev_count = best_seller[0]
if len(best_seller) > 1:
    for name, count in best_seller[1:]:
        if prev_count != count: break
        if res > name: res = name

print(res)