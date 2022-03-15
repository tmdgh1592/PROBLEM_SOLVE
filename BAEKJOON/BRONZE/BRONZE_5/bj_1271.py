import sys
input = sys.stdin.readline

N, M = map(int, input().split())
print(f'{N//M}\n{N % M}')