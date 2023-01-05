#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def f(word):
    half = n // 2

    if n % 2 == 0: return 'NOT POSSIBLE'
    if word == word[0] * n: return word[:half]
    if word[1:half+1] == word[half+1:] and word[:half] == word[half:-1]: return 'NOT UNIQUE'

    # ABXCABC
    for i in range(half):
        if word[i] != word[i + half + 1]:
            if word[i+1:half+1] == word[i + half + 1:]:
                return word[half+1:]
            else: break
    else:
        return word[:half]

    # ABAXB
    for i in range(half):
        if word[i] != word[half+i]:
            if word[i:half] == word[half+i+1:]:
                return word[:half]
            else:
                return 'NOT POSSIBLE'
    else:
        return word[:half]

n = int(input())
print(f(input().rstrip()))