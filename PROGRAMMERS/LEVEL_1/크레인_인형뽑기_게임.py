def solution(board, moves):
    answer = 0
    
    stack = []
    for move in moves:
        move -= 1
        for i in range(len(board)):
            if board[i][move] != 0:
                stack.append(board[i][move])
                board[i][move] = 0
                break
        
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                answer += 2
                stack.pop()
                stack.pop()
                
    return answer