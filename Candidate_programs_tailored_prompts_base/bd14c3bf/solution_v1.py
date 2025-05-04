def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    visited = [[False]*w for _ in range(h)]
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1 and not visited[i][j]:
                stack = [(i, j)]
                comp = []
                visited[i][j] = True
                while stack:
                    x, y = stack.pop()
                    comp.append((x, y))
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 1:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                if len(comp) >= 2:
                    for x, y in comp:
                        out[x][y] = 2
    return out