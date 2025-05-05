def solve(grid):
    h = len(grid)
    w = len(grid[0])
    row_seps = [i for i in range(h) if all(v == 0 for v in grid[i])]
    col_seps = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_regions = [(row_seps[i] + 1, row_seps[i + 1] - 1) for i in range(len(row_seps) - 1)]
    col_regions = [(col_seps[i] + 1, col_seps[i + 1] - 1) for i in range(len(col_seps) - 1)]
    out = [row[:] for row in grid]
    r0, r1 = row_regions[0]
    c0, c1 = col_regions[0]
    ih = r1 - r0 - 1
    iw = c1 - c0 - 1
    template = [[grid[r0 + i][c0 + j] for j in range(1, iw + 1)] for i in range(1, ih + 1)]
    for rr0, rr1 in row_regions:
        for cc0, cc1 in col_regions:
            for i in range(1, rr1 - rr0):
                for j in range(1, cc1 - cc0):
                    out[rr0 + i][cc0 + j] = template[i - 1][j - 1]
    return out