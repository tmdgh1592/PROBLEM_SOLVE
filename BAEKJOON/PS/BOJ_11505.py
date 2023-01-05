#-*- coding:utf-8 -*-
from math import ceil, log2
import sys
sys.setrecursionlimit(int(1e9))

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m, k = MIS()
arr = [0] + [int(input().rstrip()) for _ in range(n)]
tree = [0] * (2 ** ceil(log2(n) + 1))

def init(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return

    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007

def update(left, right, node, idx):
    if left == right == idx:
        tree[node] = arr[idx]; return
    if not (left <= idx <= right): return
    mid = (left + right) // 2
    update(left, mid, node*2, idx)
    update(mid+1, right, node*2+1, idx)
    tree[node] = (tree[node*2] * tree[node*2+1]) % 1000000007


def query(left, right, node, lidx, ridx):
    global total

    if right < lidx or ridx < left: return
    if lidx <= left and right <= ridx:
        total *= tree[node]
        return
    if lidx <= right or ridx >= left:
        mid = (left + right) // 2
        query(left, mid, node*2, lidx, ridx)
        query(mid+1, right, node*2+1, lidx, ridx)


init(1, n, 1) # 기본값 초기화

for _ in range(m+k):
    a, b, c = MIS()
    if a == 1:
        arr[b] = c
        update(1, n, 1, b)
    else:
        total = 1
        query(1, n, 1, b, c)
        print(total)