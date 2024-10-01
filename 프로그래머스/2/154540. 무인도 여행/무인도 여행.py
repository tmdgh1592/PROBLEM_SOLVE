from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    answer = []
    visited = [[False] * m for _ in range(n)]
    
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    def bfs(sx, sy):
        q = deque([(sx, sy)])
        cost = int(maps[sx][sy])
        
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if not (0 <= nx < n and 0 <= ny < m): continue
                if maps[nx][ny] == 'X': continue
                if visited[nx][ny]: continue
                q.append((nx, ny))
                visited[nx][ny] = True
                cost += int(maps[nx][ny])
    
        return cost
            
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'X': continue
            if visited[i][j]: continue
            visited[i][j] = True
            answer.append(bfs(i, j))
    
    return sorted(answer) if answer else [-1]
    