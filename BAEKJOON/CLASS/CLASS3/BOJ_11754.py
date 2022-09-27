#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())


def find_parent(parent, x):
    if x != parent[x]:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a > b: parent[a] = b
    else: parent[b] = a

n, m = MIS()
parent = [i for i in range(n+1)]
edges = [tuple(MIS()) for _ in range(m)]

for a, b in edges:
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)

result = set()
for i in range(1, n+1):
    result.add(find_parent(parent, i))

print(len(result))