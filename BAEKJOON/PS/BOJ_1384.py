#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline

def find_n(info):
    n_sequences = []
    for idx, x in enumerate(info):
        if x == 'N':
            n_sequences.append(idx)
    return n_sequences

group = 1
while(n:=int(input())):
    print(f'Group {group}')
    infos = [input().rstrip().split() for _ in range(n)]
    nasted = False
    for idx, info in enumerate(infos):
        for dist in find_n(info):
            print(f'{infos[idx - dist][0]} was nasty about {info[0]}')
            nasted = True
    
    if not nasted:
        print('Nobody was nasty')
    print()
    group += 1