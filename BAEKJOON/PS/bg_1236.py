n, m = map(int, input().split())

board = []
for _ in range(n):
    board.append(input())

row, column = 0, 0

# X가 없는 행 수를 구합니다.
for i in board:
    if 'X' not in i:
        row += 1

# X가 없는 열 수를 구합니다.
for j in range(m):
    if 'X' not in [board[i][j] for i in range(n)]:
        column += 1

# 행과 열 중에서 X가 큰 수를 출력합니다.
print(max(row, column))
