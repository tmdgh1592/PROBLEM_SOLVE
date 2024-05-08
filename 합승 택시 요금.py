def solution(n, s, a, b, fares):
    distance = [[int(1e9)] * (n + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        distance[i][i] = 0

    for x, y, cost in fares:
        distance[x][y] = cost
        distance[y][x] = cost

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

    answer = int(1e9)
    for mid in range(1, n + 1):
        answer = min(answer, distance[s][mid] + distance[mid][b] + distance[mid][a])

    return answer