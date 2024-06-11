from collections import deque

dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def solution(board):
    n = len(board)
    visited = {}

    q = deque([((0, 0), (0, 1))])
    visited[((0, 0), (0, 1))] = 0

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < n

    def can_move(node):
        cands = []
        tail, head = node

        for dx, dy in dirs:
            next_tail = (tail[0] + dx, tail[1] + dy)
            next_head = (head[0] + dx, head[1] + dy)
            if not in_range(*next_tail): continue
            if not in_range(*next_head): continue
            if board[next_tail[0]][next_tail[1]] == 0 and board[next_head[0]][next_head[1]] == 0:
                cands.append((next_tail, next_head))

        return cands

    def can_rotate(node):
        cands = []
        tail, head = node

        if node[0][0] == node[1][0]:  # 수평
            selected_dirs = dirs[2:]
        else:
            selected_dirs = dirs[:2]

        for dx, dy in selected_dirs:
            next_tail = (tail[0] + dx, tail[1] + dy)
            next_head = (head[0] + dx, head[1] + dy)

            if not in_range(*next_tail): continue
            if not in_range(*next_head): continue
            if board[next_tail[0]][next_tail[1]] == 0 and board[next_head[0]][next_head[1]] == 0:
                cands.append((tail, next_tail))
                cands.append((head, next_head))

        return cands

    while q:
        node = q.popleft()
        if node[0] == (n - 1, n - 1) or node[1] == (n - 1, n - 1):
            return visited[node]

        for cand in can_move(node) + can_rotate(node):
            if cand in visited: continue
            q.append(cand)
            visited[cand] = visited[node] + 1