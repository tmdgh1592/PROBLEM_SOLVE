# -*- coding:utf-8 -*-
def get_nexts(node):
    opers = [(-1, -2), (-2, -1), (-2, 1), (-1, 2),
             (1, 2), (2, 1), (2, -1), (1, -2)]
    alpha_to_num = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6}
    num_to_alpha = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F'}
    x, y = alpha_to_num[node[0]], int(node[1])

    ends = []
    for oper in opers:
        nx, ny = x + oper[0], y + oper[1]
        if 1 <= nx <= 6 and 1 <= ny <= 6:
            ends.append((nx, ny))

    converted_ends = []
    for end in ends:
        converted_ends.append(num_to_alpha[end[0]] + str(end[1]))

    return converted_ends


visited = dict()
start = prev = input().rstrip()
visited[prev] = True

for i in range(35):
    now = input().rstrip()
    if now not in get_nexts(prev):
        print('Invalid')
        break
    if now in visited:
        print('Invalid')
        break
    prev = now
    visited[now] = True
else:
    if start in get_nexts(prev):
        print('Valid')
    else:
        print('Invalid')