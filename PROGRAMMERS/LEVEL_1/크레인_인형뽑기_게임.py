def solution(board, moves):
    my_stack = [0]  # 인형을 담을 바구니 Stack
    n = len(board)  # 보드 N X N
    count = 0

    for move in moves:
        move -= 1

        # 선택된 인형을 집어서 Stack에 담는다.
        for i in range(n):
            if board[i][move] != 0:
                my_stack.append(board[i][move])
                board[i][move] = 0
                break

        top = len(my_stack)-1

        if len(my_stack) > 1:
            if my_stack[top] == my_stack[top-1]:
                my_stack.pop()
                my_stack.pop()
                count += 2

    return count
