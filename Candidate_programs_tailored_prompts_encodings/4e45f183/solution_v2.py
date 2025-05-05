def solve(grid):
    h = len(grid)
    w = len(grid[0])
    black_rows = [i for i in range(h) if all(v == 0 for v in grid[i])]
    black_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_intervals = [(black_rows[i] + 1, black_rows[i+1]) for i in range(len(black_rows)-1)]
    col_intervals = [(black_cols[j] + 1, black_cols[j+1]) for j in range(len(black_cols)-1)]
    out = [row[:] for row in grid]
    for r0, r1 in row_intervals:
        for c0, c1 in col_intervals:
            block = [grid[r][c0:c1] for r in range(r0, r1)]
            newb = [[0]*len(block[0]) for _ in block]
            for i in range(len(block)):
                for j in range(len(block[0])):
                    v = block[i][j]
                    if v != 0:
                        ni, nj = j, len(block)-1-i
                        newb[ni][nj] = v
            for i in range(len(block)):
                for j in range(len(block[0])):
                    out[r0+i][c0+j] = newb[i][j]
    return out