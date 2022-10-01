#-*- coding:utf-8 -*-
from bisect import bisect_left, bisect_right
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def search(num):
    left, right = bisect_left(cards, num), bisect_right(cards, num)
    return right - left

n = int(input())
cards = sorted(list(MIS()))
m = int(input())
my_cards = list(MIS())

for card in my_cards:
    print(search(card), end = ' ')