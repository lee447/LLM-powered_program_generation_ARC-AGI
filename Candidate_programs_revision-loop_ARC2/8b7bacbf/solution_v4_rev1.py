from collections import deque

def solve(grid):
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] != 0 and not visited[i][j]:
                v = grid[i][j]
                q = deque([(i, j)])
                cc = []
                visited[i][j] = True
                while q:
                    x, y = q.popleft()
                    cc.append((x, y))
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == v:
                            visited[nx][ny] = True
                            q.append((nx, ny))
                neighbor_colors = set()
                for x, y in cc:
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != v:
                            neighbor_colors.add(grid[nx][ny])
                if len(neighbor_colors) == 1 and 0 not in neighbor_colors:
                    for x, y in cc:
                        grid[x][y] = 0
    return grid