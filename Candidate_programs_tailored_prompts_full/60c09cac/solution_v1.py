def solve(grid):
    h = len(grid)
    w = len(grid[0]) if h else 0
    out = [[0] * (w * 2) for _ in range(h * 2)]
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                rr, cc = 2 * r, 2 * c
                out[rr][cc] = v
                out[rr][cc + 1] = v
                out[rr + 1][cc] = v
                out[rr + 1][cc + 1] = v
    return out