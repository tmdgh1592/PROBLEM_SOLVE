import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)


def update(i, dif):
    while i <= n:
        tree[i] += dif
        i += (i & -i)


def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        i -= (i & -i)

    return result


def interval_sum(left, right):
    return prefix_sum(right) - prefix_sum(left-1)


for i in range(1, n+1):
    x = int(input())
    arr[i] = x
    update(i, x)

for _ in range(m+k):
    a, b, c = map(int, input().split())
    if a == 1:
        # update
        update(b, c - arr[b])
        arr[b] = c
    else:
        print(interval_sum(b, c))
