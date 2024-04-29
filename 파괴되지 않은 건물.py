def solution(board, skill):
    n = len(board)
    m = len(board[0])

    delta = [[0] * (m + 1) for _ in range(n + 1)]

    for type, r1, c1, r2, c2, degree in skill:
        degree = degree if type == 2 else -degree
        delta[r1][c1] += degree
        delta[r2 + 1][c2 + 1] += degree
        delta[r2 + 1][c1] -= degree
        delta[r1][c2 + 1] -= degree

    for c in range(m):
        for r in range(1, n):
            delta[r][c] += delta[r - 1][c]

    for r in range(n):
        for c in range(1, m):
            delta[r][c] += delta[r][c - 1]

    answer = 0
    for r in range(n):
        for c in range(m):
            board[r][c] += delta[r][c]
            if board[r][c] > 0:
                answer += 1

    return answer