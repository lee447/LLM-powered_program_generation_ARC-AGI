def solve(grid: list[list[int]]) -> list[list[int]]:
    h = len(grid)
    w = len(grid[0]) if h else 0
    res = [row[:] for row in grid]
    visited = [[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                comp = [(i, j)]
                visited[i][j] = True
                idx = 0
                while idx < len(stack):
                    x, y = stack[idx]
                    idx += 1
                    for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx, ny = x+dx, y+dy
                        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and grid[nx][ny] == 0:
                            visited[nx][ny] = True
                            stack.append((nx, ny))
                            comp.append((nx, ny))
                if len(comp) > 1:
                    for x, y in comp:
                        res[x][y] = 8
    return res