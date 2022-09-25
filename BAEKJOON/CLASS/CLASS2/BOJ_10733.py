#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

stack = []
for _ in range(int(input())):
    money = int(input())
    stack.append(money) if money else stack.pop()

print(sum(stack))