trans = {'E': 0, 'W': 1, 'S': 2, 'N': 3}
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def solution(park, routes):
    graph = []
    width = len(park[0])
    height = len(park)

    for i, p in enumerate(park):
        row = list(p)
        graph.append(row)
        if 'S' in row:
            r, c = i, row.index('S')

    for route in routes:
        dir, dist = route.split()[0], int(route.split()[1])
        dir = trans[dir]

        ddx, ddy = dx[dir], dy[dir]
        if not (0 <= r + ddx * dist < height and 0 <= c + ddy * dist < width): continue
        tmp_r, tmp_c = r, c

        flag = False
        for _ in range(dist):
            tmp_r += ddx
            tmp_c += ddy

            if graph[tmp_r][tmp_c] == 'X':
                flag = True
                break

        if not flag:
            r += ddx * dist
            c += ddy * dist

    return [r, c]
