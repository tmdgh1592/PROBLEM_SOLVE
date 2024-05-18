INF = int(1e9)


def solution(n, results):
    graph = [[INF] * n for _ in range(n)]
    for i in range(n + 1):
        graph[i - 1][i - 1] = 0

    for a, b in results:
        graph[a - 1][b - 1] = 1
        graph[b - 1][a - 1] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1
                    graph[j][i] = 0

    answer = 0
    for row in graph:
        if INF in row: continue
        answer += 1
    return answer
