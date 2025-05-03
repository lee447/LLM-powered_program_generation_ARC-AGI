def solve(grid):
    h, w = len(grid), len(grid[0])
    row_counts = [sum(1 for v in row if v != 0) for row in grid]
    col_counts = [sum(1 for r in range(h) if grid[r][c] != 0) for c in range(w)]
    rm = max(row_counts)
    cm = max(col_counts)
    rt = rm // 2
    ct = cm // 2
    keep_r = [i for i, c in enumerate(row_counts) if c > rt]
    keep_c = [j for j, c in enumerate(col_counts) if c > ct]
    out = [[0]*w for _ in range(h)]
    for i in keep_r:
        for j in keep_c:
            out[i][j] = grid[i][j]
    return out