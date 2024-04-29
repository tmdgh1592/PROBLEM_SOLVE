def solution(m, n, board):
    answer = 0
    board = [list(row) for row in board]

    while True:

        will_remove = []
        for i in range(m - 1):
            for j in range(n - 1):
                if board[i][j] == board[i + 1][j] == board[i + 1][j + 1] == board[i][j + 1] and board[i][j] != "":
                    will_remove.extend([(i, j), (i + 1, j), (i, j + 1), (i + 1, j + 1)])

        for x, y in will_remove:
            board[x][y] = ""

        for _ in range(m):
            for i in range(m - 1):
                for j in range(n):
                    if board[i + 1][j] == "":
                        board[i + 1][j] = board[i][j]
                        board[i][j] = ""

        if not will_remove:
            for i in range(m):
                for j in range(n):
                    if board[i][j] == "":
                        answer += 1
            return answer