n = int(input())
graph = [list(input()) for _ in range(n)]

colors = ['C', 'P', 'Z', 'Y']
max_cnt = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0,0,-1,1]

def get_max_same_row(graph, row):
    #color_dict = {'C':0, 'P':0,'Z':0,'Y':0}
    max_cnt = 1
    temp_cnt = 1
    for i in range(n-1):
        if graph[row][i] == graph[row][i+1]:
            temp_cnt += 1
            max_cnt = max(max_cnt, temp_cnt)
        else:
            temp_cnt = 1

    return max_cnt

def get_max_same_col(graph, col):
    #color_dict = {'C':0, 'P':0,'Z':0,'Y':0}
    max_cnt = 1
    temp_cnt = 1
    for i in range(n-1):
        if graph[i][col] == graph[i+1][col]:
            temp_cnt += 1
            max_cnt = max(max_cnt, temp_cnt)
        else:
            temp_cnt = 1

    return max_cnt

def check(graph, x,y,nx,ny):
    return max(get_max_same_row(graph, x), get_max_same_row(graph, nx), get_max_same_col(graph, y), get_max_same_col(graph, ny))

for row in range(n):
    for col in range(n):
        for i in range(4):
            nx, ny = row+dx[i], col+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 스왑
                graph[nx][ny], graph[row][col] = graph[row][col], graph[nx][ny]
                max_cnt = max(max_cnt, check(graph, row, col, nx, ny))
                graph[nx][ny], graph[row][col] = graph[row][col], graph[nx][ny]

print(max_cnt)