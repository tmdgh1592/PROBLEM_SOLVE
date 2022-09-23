from math import ceil, log2
import sys
sys.setrecursionlimit(int(1e9))

n = 4
arr = [0] + [1,2,3,4]
tree = [0] * (pow(2, ceil(log2(n) + 1)))
answer = 0

def init(left, right, node):
    if left == right:
        tree[node] = arr[left]
        return

    mid = (left + right) // 2
    init(left, mid, node*2)
    init(mid+1, right, node*2+1)
    tree[node] = tree[node*2] + tree[node*2+1]

def update(left, right, node, idx, val):
    if left == right == idx:
        tree[node] = val
        return
    if not (left <= node <= right): return
    
    mid = (left + right) // 2
    update(left, mid, node*2, idx, val)
    update(mid+1, right, node*2+1, idx, val)
    tree[node] = tree[node*2] + tree[node*2+1]

def query(left, right, node, lidx, ridx):
    global answer

    if lidx > right or ridx < left: return
    if lidx <= left and right <= ridx:
        answer += tree[node]
        return
    if lidx <= right or ridx >= left:
        mid = (left + right) // 2
        query(left, mid, node*2, lidx, ridx)
        query(mid+1, right, node*2+1, lidx, ridx)

init(1, n, 1)
update(1, n, 1, 2, 10)
query(1, n, 1, 1, n)
print(answer)