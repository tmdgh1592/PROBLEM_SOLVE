from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]


def find_blocks(board, type):
    blocks = []
    n = len(board)
    visited = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and board[i][j] == type:
                q = deque([(i, j)])
                visited[i][j] = True
                lst = [(i, j)]

                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if not ((0 <= nx < n) and (0 <= ny < n)):
                            continue
                        if not visited[nx][ny] and board[nx][ny] == type:
                            q.append((nx, ny))
                            visited[nx][ny] = True
                            lst.append((nx, ny))
                blocks.append(lst)
    return blocks


def make_table(block):
    xs, ys = zip(*block)
    c, r = max(xs) - min(xs) + 1, max(ys) - min(ys) + 1
    table = [[0] * r for _ in range(c)]

    for i, j in block:
        i, j = i - min(xs), j - min(ys)
        table[i][j] = 1
    return table


def rotate(puzzle):
    rotate = [[0] * len(puzzle) for _ in range(len(puzzle[0]))]
    count = 0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[0])):
            if puzzle[i][j] == 1:
                count += 1
            rotate[len(puzzle[0]) - 1 - j][i] = puzzle[i][j]
    return rotate, count


def solution(game_board, table):
    answer = 0

    empties = find_blocks(game_board, 0)
    puzzles = find_blocks(table, 1)

    for empty in empties:

        empty_table = make_table(empty)
        flag = False
        for puzzle in puzzles:
            puzzle_table = make_table(puzzle)
            for rot in range(4):
                puzzle_table, count = rotate(puzzle_table)

                if puzzle_table == empty_table:
                    answer += count
                    puzzles.remove(puzzle)
                    flag = True
                    break
            if flag:
                break

    return answer
