#-*- coding:utf-8 -*-
import sys

sys.stdin = open('input.txt', 'r')
input = sys.stdin.readline
MIS = lambda: map(int, input().rstrip().split())

n, m = MIS()
arr = [list(map(int, input().rstrip())) for _ in range(n)]
result = -sys.maxsize

# 1 : 가로
# 0 : 세로
for i in range(1 << (n * m)):
    temp_result = 0

    for row in range(n):
        row_sum = 0
        for col in range(m):
            cursor = row * m + col

            if i & (1 << cursor):
                row_sum = row_sum * 10 + arr[row][col]
            else:
                temp_result += row_sum
                row_sum = 0

        temp_result += row_sum

    for col in range(m):
        col_sum = 0
        for row in range(n):
            cursor = row * m + col

            if not (i & (1 << cursor)):
                col_sum = col_sum * 10 + arr[row][col]
            else:
                temp_result += col_sum
                col_sum = 0

        temp_result += col_sum

    result = max(result, temp_result)

print(result)