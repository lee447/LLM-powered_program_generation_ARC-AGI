def solve(grid):
    h = len(grid)
    w = len(grid[0])
    out = [[0] * (w * 2) for _ in range(h * 2)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            out[2*r][2*c] = v
            out[2*r][2*c+1] = v
            out[2*r+1][2*c] = v
            out[2*r+1][2*c+1] = v
    return out