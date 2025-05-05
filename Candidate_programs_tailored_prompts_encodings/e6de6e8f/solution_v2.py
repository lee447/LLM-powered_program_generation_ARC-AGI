def solve(grid):
    rows, cols = len(grid), len(grid[0])
    anchor = 3
    row1_cols = [c for c in range(cols) if grid[1][c] == 2 and c != anchor]
    row1_cols.sort()
    out_h, out_w = 8, 7
    out = [[0]*out_w for _ in range(out_h)]
    out[0][anchor] = 3
    cur = anchor
    r = 1
    for c in row1_cols:
        if c > anchor:
            cur += 1
        if grid[0][c] == 2:
            out[r][cur] = 2
            if cur+1 < out_w:
                out[r][cur+1] = 2
        else:
            out[r][cur] = 2
        r += 1
    return out