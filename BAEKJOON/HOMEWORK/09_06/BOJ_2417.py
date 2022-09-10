import sys

#sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
lo, hi = 0, n

while lo <= hi:
    mid = (lo + hi) // 2
    if mid**2 >= n:
        hi = mid - 1
    else:
        lo = mid + 1

print(lo)