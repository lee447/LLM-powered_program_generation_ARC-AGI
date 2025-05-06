def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    orig = grid
    res = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            col = orig[i][j]
            if col > 1:
                stack = [(i, j)]
                while stack:
                    x, y = stack.pop()
                    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < h and 0 <= ny < w and orig[nx][ny] == 0 and res[nx][ny] == 0:
                            res[nx][ny] = col
                            stack.append((nx, ny))
    return res