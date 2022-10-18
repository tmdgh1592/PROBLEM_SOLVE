#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

word = input().rstrip()

for i in range(len(word)):
    sub_word = word[i:]
    if sub_word == sub_word[::-1]:
        print(len(word) + i)
        break