def solve(grid):
    n = len(grid)
    sep_rows = [i for i in range(n) if all(c == 0 for c in grid[i])]
    sep_cols = [j for j in range(n) if all(grid[i][j] == 0 for i in range(n))]
    row_intervals = [(sep_rows[i] + 1, sep_rows[i + 1]) for i in range(len(sep_rows) - 1)]
    col_intervals = [(sep_cols[i] + 1, sep_cols[i + 1]) for i in range(len(sep_cols) - 1)]
    row_intervals = row_intervals[0:3]
    col_intervals = col_intervals[0:3]
    blocks = []
    for ri, rj in row_intervals:
        row = []
        for ci, cj in col_intervals:
            blk = [grid[r][ci:cj] for r in range(ri, rj)]
            row.append(blk)
        blocks.append(row)
    new_blocks = [[blocks[j][i] for j in range(3)] for i in range(3)]
    res = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 0:
                res[i][j] = 0
    for bi in range(3):
        ri, rj = row_intervals[bi]
        for bj in range(3):
            ci, cj = col_intervals[bj]
            blk = new_blocks[bi][bj]
            for di in range(rj - ri):
                for dj in range(cj - ci):
                    res[ri + di][ci + dj] = blk[di][dj]
    return res