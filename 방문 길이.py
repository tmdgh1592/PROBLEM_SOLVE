from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
dir_dict = ['U', 'D', 'L', 'R']


def solution(dirs):
    routes = set()
    q = deque([(0, 0, 0)])

    while q:
        x, y, i = q.popleft()

        if i == len(dirs): break
        d = dir_dict.index(dirs[i])
        nx, ny = x + dx[d], y + dy[d]

        if not (-5 <= nx <= 5 and -5 <= ny <= 5):
            q.append((x, y, i + 1))
        else:
            routes.add(f'{x}{y}{nx}{ny}')
            routes.add(f'{nx}{ny}{x}{y}')
            q.append((nx, ny, i + 1))

    return len(routes) // 2