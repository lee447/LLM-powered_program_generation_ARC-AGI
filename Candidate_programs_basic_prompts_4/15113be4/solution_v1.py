def solve(grid):
    R, C = len(grid), len(grid[0])
    wall_rows = [all(grid[r][c] == 4 for c in range(C)) for r in range(R)]
    wall_cols = [all(grid[r][c] == 4 for r in range(R)) for c in range(C)]
    block_h = wall_rows.index(True)
    block_w = wall_cols.index(True)
    period_h = block_h + 1
    period_w = block_w + 1
    colors = set(grid[r][c] for r in range(R) for c in range(C))
    c = next(col for col in colors if col not in (0,1,4))
    # find one occurrence
    for i in range(R):
        for j in range(C):
            if grid[i][j] == c:
                i0, j0 = i, j
                break
        else:
            continue
        break
    by0 = i0 // period_h
    bx0 = j0 // period_w
    base_i = by0 * period_h
    base_j = bx0 * period_w
    mask = []
    for i in range(base_i, base_i + block_h):
        for j in range(base_j, base_j + block_w):
            if grid[i][j] == c:
                mask.append((i - base_i, j - base_j))
    out = [row[:] for row in grid]
    for br in range(R // period_h + 1):
        for bc in range(C // period_w + 1):
            start_i = br * period_h
            start_j = bc * period_w
            for di, dj in mask:
                ti, tj = start_i + di, start_j + dj
                if 0 <= ti < R and 0 <= tj < C and grid[ti][tj] == 1:
                    out[ti][tj] = c
    return out