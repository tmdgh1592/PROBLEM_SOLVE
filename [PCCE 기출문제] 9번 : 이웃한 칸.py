def solution(board, h, w):
    dh, dw = [0, 1, -1, 0], [1, 0, 0, -1]
    count = 0
    n = len(board)
    board_color = board[h][w]

    for i in range(4):
        nh, nw = h + dh[i], w + dw[i]
        if not (0 <= nh < n and 0 <= nw < n): continue
        if board[nh][nw] == board_color:
            count += 1

    return count
