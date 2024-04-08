from collections import deque

dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]
dirs = {0:'d', 1:'l', 2:'r', 3:'u'}

def in_range(n, m, x, y):
    return 0 <= x < n and 0 <= y < m

def solution(n, m, sx, sy, ex, ey, k):
    sx, sy, ex, ey = sx-1, sy-1, ex-1, ey-1
    q = deque([(sx, sy, '')])
    
    while q:
        x, y, command = q.popleft()
        
        if len(command) == k and x == ex and y == ey: return command
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            path = command + dirs[i]
            if not in_range(n, m, nx, ny): continue
            if k - len(path) < abs(nx - ex) + abs(ny - ey): continue
            q.append((nx, ny, path))
            break
    
    return "impossible"
