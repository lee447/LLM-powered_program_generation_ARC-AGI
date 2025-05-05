def solve(grid):
    H = len(grid)
    W = len(grid[0])
    zero_rows = [i for i in range(H) if all(grid[i][j] == 0 for j in range(W))]
    row_segs = []
    for a, b in zip(zero_rows, zero_rows[1:]):
        if b - a > 1:
            row_segs.append((a + 1, b - 1))
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    col_segs = []
    for a, b in zip(zero_cols, zero_cols[1:]):
        if b - a > 1:
            col_segs.append((a + 1, b - 1))
    out = [row[:] for row in grid]
    if not row_segs or not col_segs:
        return out
    top_r0, top_r1 = row_segs[0]
    bot_r0, bot_r1 = row_segs[-1]
    for c0, c1 in col_segs:
        if top_r1 - top_r0 != bot_r1 - bot_r0 or c1 - c0 != 4:
            continue
        pattern = []
        for dr in range(1, 4):
            for dc in range(1, 4):
                if grid[top_r0 + dr][c0 + dc] != 0:
                    pattern.append((dr - 1, dc - 1))
        if not pattern:
            continue
        color = grid[bot_r0][c0]
        for dr0, dc0 in pattern:
            rr = bot_r0 + 1 + dr0
            cc = c0 + 1 + dc0
            out[rr][cc] = color
            for ddr, ddc in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                nr, nc = rr + ddr, cc + ddc
                if bot_r0 + 1 <= nr <= bot_r0 + 3 and c0 + 1 <= nc <= c0 + 3:
                    out[nr][nc] = color
    return out