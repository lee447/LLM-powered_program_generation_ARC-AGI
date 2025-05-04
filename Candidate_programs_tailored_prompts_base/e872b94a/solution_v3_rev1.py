from collections import deque

def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 5 and not visited[i][j]:
                count += 1
                q = deque([(i, j)])
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 5:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    return [[0] for _ in range(count)]