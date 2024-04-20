def solution(begin, target):
    answer = float('inf')
    r, c = len(begin), len(begin[0])

    for bit in range(1 << (r + c)):
        board = [row[:] for row in begin]
        cnt = bin(bit).count('1')
        if cnt >= answer: continue

        for i in range(r):
            if bit & (1 << i):
                board[i] = [not c for c in board[i]]
        for i in range(c):
            if bit & (1 << (r + i)):
                for row in range(r):
                    board[row][i] = not board[row][i]

        if target == board:
            answer = min(answer, cnt)

    return -1 if answer == float('inf') else answer