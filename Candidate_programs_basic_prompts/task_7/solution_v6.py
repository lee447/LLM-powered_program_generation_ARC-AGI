def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    sep_rows = [r for r in range(rows) if all(grid[r][c] == grid[r][0] for c in range(cols))]
    sep_cols = [c for c in range(cols) if all(grid[r][c] == grid[0][c] for r in range(rows))]
    def segments(seps, n):
        segs = []
        prev = -1
        for s in seps + [n]:
            if s - prev > 1:
                segs.append((prev + 1, s - 1))
            prev = s
        return segs
    row_segs = segments(sep_rows, rows)
    col_segs = segments(sep_cols, cols)
    block_h = row_segs[0][1] - row_segs[0][0] + 1
    block_w = col_segs[0][1] - col_segs[0][0] + 1
    sep_color = grid[sep_rows[0]][0] if sep_rows else None
    vals = {grid[r][c] for r in range(rows) for c in range(cols)}
    fill_colors = [v for v in vals if v not in (0,1,sep_color)]
    fill_color = fill_colors[0] if fill_colors else None
    initial = set()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == fill_color:
                bi = next(i for i,(a,b) in enumerate(row_segs) if a <= r <= b)
                bj = next(j for j,(a,b) in enumerate(col_segs) if a <= c <= b)
                initial.add((bi,bj))
    out = [row[:] for row in grid]
    for bi,bj in initial:
        if bi > bj:
            ti, tj = bj, bi
            r0, _ = row_segs[ti]
            c0, _ = col_segs[tj]
            for dr in range(block_h):
                for dc in range(block_w):
                    rr, cc = r0 + dr, c0 + dc
                    if grid[rr][cc] == 1:
                        out[rr][cc] = fill_color
    return out