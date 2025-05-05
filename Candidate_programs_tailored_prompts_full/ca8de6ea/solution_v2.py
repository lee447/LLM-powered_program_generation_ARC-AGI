def solve(grid):
    h = len(grid)
    if h == 0: return []
    w = len(grid[0])
    out_h = h // 2 + 1
    out_w = w // 2 + 1
    out = [[0] * out_w for _ in range(out_h)]
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                out[i // 2][j // 2] = v
    return out