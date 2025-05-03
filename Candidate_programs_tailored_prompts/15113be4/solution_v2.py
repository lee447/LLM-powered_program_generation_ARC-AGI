def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(grid[i][j] == 4 for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 4 for i in range(h))]
    row_blocks = [(sep_rows[i] + 1, sep_rows[i+1] - sep_rows[i] - 1) for i in range(len(sep_rows)-1)]
    col_blocks = [(sep_cols[i] + 1, sep_cols[i+1] - sep_cols[i] - 1) for i in range(len(sep_cols)-1)]
    motif = None
    for br, bh in row_blocks:
        for bc, bw in col_blocks:
            coords = [(r-br, c-bc, grid[r][c]) for r in range(br, br+bh) for c in range(bc, bc+bw)
                      if grid[r][c] not in (0,1,4)]
            if coords:
                motif = (coords[0][2], [(dr, dc) for dr, dc, v in coords])
                mr, mc = br, bc
                break
        if motif: break
    color, rel = motif
    out = [row[:] for row in grid]
    for br, bh in row_blocks:
        for bc, bw in col_blocks:
            if br == mr and bc == mc: continue
            for dr, dc in rel:
                r, c = br+dr, bc+dc
                if out[r][c] == 0:
                    out[r][c] = color
    return out