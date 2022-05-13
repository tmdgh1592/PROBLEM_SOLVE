import sys
sys.setrecursionlimit(10 ** 6)

n = int(input())
star = [['*'] * n for _ in range(n)]
visited = [[False] * n for _ in range(n)]

def draw_star(n, x, y, interval):
    if x >= n or y >= n or visited[x][y]:
        return

    visited[x][y] = True

    draw_empty(x, y, x+interval, y+interval) # 현재 x, y 위치에서 interval만큼의 정사각형 공백을 그린다.
    draw_star(n, x+3*interval, y, interval) # x축 좌표 이동
    draw_star(n, x, y+3*interval, interval) # y축 좌표 이동
    draw_star(n, x*3, y*3, 3 * interval) # x, y축 좌표 이동

def draw_empty(x, y, x_limit, y_limit):
    star[x][y] = ' '
    visited[x][y] = True

    if x + 1 < x_limit and x+1 < n and y < n:
        if not visited[x+1][y]:
            draw_empty(x+1, y, x_limit, y_limit)
    if y + 1 < y_limit and y < n and y+1 < n:
        if not visited[x][y+1]:
            draw_empty(x, y+1, x_limit, y_limit)

draw_star(n, 1, 1, 1)

for i in range(n):
    print(*star[i], sep='')