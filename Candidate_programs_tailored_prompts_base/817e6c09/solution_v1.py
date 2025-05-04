def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    for r in range(H - 1):
        for c in range(W - 1):
            if grid[r][c] == 2 and grid[r][c+1] == 2 and grid[r+1][c] == 2 and grid[r+1][c+1] == 2:
                color = 8 if (r + c) <= (W - 1) else 2
                out[r][c] = color
                out[r][c+1] = color
                out[r+1][c] = color
                out[r+1][c+1] = color
    return out