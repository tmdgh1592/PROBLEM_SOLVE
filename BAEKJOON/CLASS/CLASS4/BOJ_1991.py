#-*- coding:utf-8 -*-
from collections import defaultdict
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

def preorder(idx):
    if tree[idx] != '.': print(tree[idx], end='')
    if tree[idx * 2] != '.': preorder(idx * 2)
    if tree[idx * 2 + 1] != '.': preorder(idx * 2 + 1)

def inorder(idx):
    if tree[idx * 2] != '.': inorder(idx * 2)
    if tree[idx] != '.': print(tree[idx], end='')
    if tree[idx * 2 + 1] != '.': inorder(idx * 2 + 1)

def postorder(idx):
    if tree[idx * 2] != '.': postorder(idx * 2)
    if tree[idx * 2 + 1] != '.': postorder(idx * 2 + 1)
    if tree[idx] != '.': print(tree[idx], end='')

nodes_idx = defaultdict(int)
n = int(input())
tree = ['.'] * 1000
idx = 1
for _ in range(n):
    root, left, right = input().rstrip().split()
    idx = 1 if nodes_idx[root] == 0 else nodes_idx[root]
    nodes_idx[root] = idx
    nodes_idx[left] = idx * 2
    nodes_idx[right] = idx * 2 + 1
    tree[idx] = root
    tree[idx * 2] = left
    tree[idx * 2 + 1] = right


preorder(1); print()
inorder(1); print()
postorder(1); print()