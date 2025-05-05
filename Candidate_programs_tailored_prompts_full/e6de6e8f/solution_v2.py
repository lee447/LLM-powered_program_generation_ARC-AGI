def solve(grid):
    steps = []
    h, w = len(grid), len(grid[0])
    for col in range(w):
        c = 0
        if grid[0][col] == 2: c += 1
        if grid[1][col] == 2: c += 1
        if c > 0:
            steps.append(2 if c == 2 else 1)
    out_h, out_w = 8, 7
    out = [[0]*out_w for _ in range(out_h)]
    out[0][3] = 3
    r, c = 1, 3
    for step in steps:
        if r >= out_h: break
        if step == 2:
            if c+1 < out_w:
                out[r][c] = 2
                out[r][c+1] = 2
            else:
                out[r][c] = 2
        else:
            out[r][c] = 2
        r += 1
        c = min(c+1, out_w-1)
    return out