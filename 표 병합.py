table = [["EMPTY"] * 51 for _ in range(51)]
parent = [[(r, c) for c in range(51)] for r in range(51)]


def find(r, c):
    if (r, c) != parent[r][c]:
        pr, pc = parent[r][c]
        return find(pr, pc)
    return (r, c)


def union(r1, c1, r2, c2):
    parent[r2][c2] = parent[r1][c1]


def update(r, c, value):
    pr, pc = find(r, c)
    table[pr][pc] = value


def update_val(value1, value2):
    for i in range(51):
        for j in range(51):
            pr, pc = find(i, j)
            if table[pr][pc] == value1:
                table[pr][pc] = value2


def merge(r1, c1, r2, c2):
    r1, c1 = find(r1, c1)
    r2, c2 = find(r2, c2)

    if (r1, c1) == (r2, c2):
        return
    elif table[r1][c1] != "EMPTY":
        union(r1, c1, r2, c2)
    else:
        union(r2, c2, r1, c1)


def unmerge(r, c):
    pr, pc = find(r, c)
    val = table[pr][pc]
    merges = []
    for i in range(51):
        for j in range(51):
            if find(i, j) == (pr, pc):
                merges.append((i, j))

    for x, y in merges:
        parent[x][y] = (x, y)
        table[x][y] = "EMPTY" if (x, y) != (r, c) else val


def solution(commands):
    answer = []

    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == "UPDATE" and len(cmd) == 4:
            update(int(cmd[1]), int(cmd[2]), cmd[3])
        if cmd[0] == "UPDATE" and len(cmd) == 3:
            update_val(cmd[1], cmd[2])
        if cmd[0] == "MERGE":
            merge(int(cmd[1]), int(cmd[2]), int(cmd[3]), int(cmd[4]))
        if cmd[0] == "UNMERGE":
            unmerge(int(cmd[1]), int(cmd[2]))
        if cmd[0] == "PRINT":
            pr, pc = find(int(cmd[1]), int(cmd[2]))
            answer.append(table[pr][pc])

    return answer