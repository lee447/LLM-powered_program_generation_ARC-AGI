def solve(grid):
    H = len(grid)
    W = len(grid[0])
    out = [row[:] for row in grid]
    fours = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    for r, c in fours:
        r2 = H - 1 - r
        if out[r2][c] != 4:
            out[r2][c] = 4
        c2 = W - 1 - c
        if out[r][c2] != 4:
            out[r][c2] = 4
    return out