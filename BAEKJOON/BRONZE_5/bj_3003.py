import sys
input = sys.stdin.readline

piece_list = [1, 1, 2, 2, 2, 8]
has_piece = list(map(int, input().split()))

for i in range(6):
    print(piece_list[i] - has_piece[i], end=' ')
