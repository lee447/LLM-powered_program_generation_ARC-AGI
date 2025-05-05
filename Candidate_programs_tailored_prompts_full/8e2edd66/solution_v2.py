def solve(grid):
    h = len(grid)
    w = len(grid[0])
    mask = [[grid[r][c] == 0 for c in range(w)] for r in range(h)]
    color = next(grid[r][c] for r in range(h) for c in range(w) if grid[r][c] != 0)
    out = [[0] * (w * w) for _ in range(h * h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 0:
                bi = i * h
                bj = j * w
                for r in range(h):
                    for c in range(w):
                        if mask[r][c]:
                            out[bi + r][bj + c] = color
    return out