def solution(board):
    o, x = 0, 0
    owin, xwin = False, False
    
    for row in board:
        for r in row:
            if r == 'O': o += 1
            if r == 'X': x += 1
    
    if board[0][:] == 'OOO' or board[1][:] == 'OOO' or board[2][:] == 'OOO':
        owin = True
    if board[0][0]+board[1][0]+board[2][0] == 'OOO' or board[0][1]+board[1][1]+board[2][1] == 'OOO' or board[0][2]+board[1][2]+board[2][2] == 'OOO':
        owin = True
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        owin = True
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        owin = True
    if board[0][:] == 'XXX' or board[1][:] == 'XXX' or board[2][:] == 'XXX':
        xwin = True
    if board[0][0]+board[1][0]+board[2][0] == 'XXX' or board[0][1]+board[1][1]+board[2][1] == 'XXX' or board[0][2]+board[1][2]+board[2][2] == 'XXX':
        xwin = True
    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        xwin = True
    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        xwin = True
    
    if o >= x + 2: return 0
    if owin and xwin: return 0
    if owin and o == x: return 0
    if xwin and o != x: return 0
    
    return 1
