from collections import defaultdict
from math import trunc


def solution(str1, str2):
    a, b = defaultdict(int), defaultdict(int)
    mset = set()

    for i in range(len(str1) - 1):
        text = str1[i:i + 2].lower()
        if text.isalpha():
            a[text] += 1
            mset.add(text)

    for i in range(len(str2) - 1):
        text = str2[i:i + 2].lower()
        if text.isalpha():
            b[text] += 1
            mset.add(text)

    x, y = 0, 0
    for key in mset:
        x += min(a[key], b[key])
        y += max(a[key], b[key])

    if x == 0 and y == 0: return 65536
    return trunc(65536 * x / y)