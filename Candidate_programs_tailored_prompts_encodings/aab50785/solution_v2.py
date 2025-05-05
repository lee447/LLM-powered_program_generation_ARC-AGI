def solve(grid):
    R, C = len(grid), len(grid[0])
    bands = []
    for r in range(R - 1):
        cs = []
        for c in range(C - 1):
            if grid[r][c] == 8 and grid[r][c+1] == 8 and grid[r+1][c] == 8 and grid[r+1][c+1] == 8:
                cs.append(c)
        if len(cs) >= 2:
            bands.append((r, cs[0], cs[1]))
    out = []
    for r, c1, c2 in bands:
        start_c = c1 + 2
        end_c = c2 - 1
        for rr in (r, r + 1):
            row = []
            for cc in range(start_c, end_c + 1):
                v = grid[rr][cc]
                row.append(v if v != 8 else 0)
            out.append(row)
    return out