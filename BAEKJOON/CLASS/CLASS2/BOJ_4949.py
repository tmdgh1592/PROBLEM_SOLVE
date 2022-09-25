#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
table = {')':'(', ']':'['}

while (s:=input().rstrip()) != '.':
    stack = []

    for ch in s:
        if ch in ['(', '[']: stack.append(ch)
        elif ch in table:
            if not stack or table[ch] != stack.pop():
                print('no'); break
    else: print('no' if stack else 'yes')