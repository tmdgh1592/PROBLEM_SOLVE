# 현재 이동횟수가 k-1인데 다음 이동칸이 평지가 아닌 경우 고려.
# 현재 이동횟수가 k-1인데 다음 이동칸이 평지면 이동해서 카운트 증가

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0
count = -1


def solution(graph, k):
    visited = [[False] * len(graph[0]) for _ in range(len(graph))]
    dfs(graph, 0, 0, k, visited)
    return result


def dfs(graph, x, y, k, visited):
    global result
    global count

    # 방문했는데 count가 k+1이고 평지가 아니라면
    if count == k+1 and graph[x][y] != '.':
        # 또한, 목적지가 아니라면 False
        if x != len(graph) - 1 and y != len(graph[0]) - 1:
            return False
    elif count == k+1 and graph[x][y] == '.':
        result += 1
        count = 0


    if not visited[x][y]:
        visited[x][y] = True
        count += 1

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if (0 <= nx < len(graph) and 0 <= ny < len(graph[0])):  # 범위 체크
                if graph[nx][ny] != '#':  # 숲이 아니라면
                    # 다음 위치 방문했는데 야영해야 하지만, 야영할 수 있는 곳이 아님
                    if dfs(graph, nx, ny, k, visited) == False:
                        visited[nx][ny] = False
                        if graph[x][y] != '.':  # 지금 위치도 야영할 수 있는 곳이 아님
                            return False  # return False
                        else:  # 지금 위치는 야영 가능함
                            result += 1
                            count = 0
