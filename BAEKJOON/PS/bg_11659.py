import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

prefix = 0
prefix_sum = [0]

for x in arr:
    prefix += x
    prefix_sum.append(prefix)


def interval_sum(left, right):
    return prefix_sum[right] - prefix_sum[left-1]


for _ in range(m):
    a, b = map(int, input().split())
    print(interval_sum(a, b))
