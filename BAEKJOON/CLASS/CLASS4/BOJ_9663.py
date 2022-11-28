#-*- coding:utf-8 -*-
import sys
sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n = int(input())
board = [0] * n
visited = [False] * n

def check(col):
    for prev in range(col):
        # 대각선 체크 예시) (3, 3), (2, 2)에서 3 - 2 == 3 - 2
        if abs(col - prev) == abs(board[col] - board[prev]):
            return False
    return True

def f(col):
    res = 0
    
    if col == n: return 1
    for row in range(n):
        if visited[row]: continue
        
        board[col] = row
        if check(col): # row, col에 둘 수 있는가
            visited[row] = True
            res += f(col + 1)
            visited[row] = False
    return res

print(f(0))