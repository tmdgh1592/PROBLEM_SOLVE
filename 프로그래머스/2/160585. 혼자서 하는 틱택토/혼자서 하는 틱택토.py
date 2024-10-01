def solution(board):
    # [실패 case]
    # 두 돌의 개수 차이가 1보다 큰 경우
    # X가 O보다 많은 경우
    # 둘다 이긴 경우
    # 
    
    o_cnt, x_cnt = 0, 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'O': o_cnt += 1
            elif board[i][j] == 'X': x_cnt += 1
    
    # 게임 승리 조건 판단()
    def is_win(symbol):
        if board[0] == symbol * 3: return True
        if board[1] == symbol * 3: return True
        if board[2] == symbol * 3: return True
        if board[0][0] + board[1][0] + board[2][0] == symbol * 3: return True
        if board[0][1] + board[1][1] + board[2][1] == symbol * 3: return True
        if board[0][2] + board[1][2] + board[2][2] == symbol * 3: return True
        if board[0][0] + board[1][1] + board[2][2] == symbol * 3: return True
        if board[0][2] + board[1][1] + board[2][0] == symbol * 3: return True
        return False

    if abs(o_cnt - x_cnt) > 1: return 0
    if x_cnt > o_cnt: return 0
    if is_win('O') and is_win('X'): return 0
    if is_win('O') and o_cnt != x_cnt + 1: return 0
    if is_win('X') and o_cnt != x_cnt: return 0

    return 1
        