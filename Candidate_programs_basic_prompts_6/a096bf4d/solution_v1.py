def solve(grid):
    h, w = len(grid), len(grid[0])
    sep_rows = [i for i in range(h) if all(grid[i][j] == 0 for j in range(w))]
    sep_cols = [j for j in range(w) if all(grid[i][j] == 0 for i in range(h))]
    row_ranges = [(sep_rows[i] + 1, sep_rows[i+1] - 1) for i in range(len(sep_rows)-1)]
    col_ranges = [(sep_cols[j] + 1, sep_cols[j+1] - 1) for j in range(len(sep_cols)-1)]
    for br, (rs, re) in enumerate(row_ranges):
        c0s, c0e = col_ranges[0]
        freq = {}
        for i in range(rs, re+1):
            for j in range(c0s, c0e+1):
                v = grid[i][j]
                if v:
                    freq[v] = freq.get(v, 0) + 1
        extras = [c for c, cnt in freq.items() if cnt == 1]
        if len(extras) == 1:
            c_extra = extras[0]
            for i in range(rs, re+1):
                for j in range(c0s, c0e+1):
                    if grid[i][j] == c_extra:
                        r_loc, c_loc = i - rs, j - c0s
                        break
                else:
                    continue
                break
            for bc, (cs, ce) in enumerate(col_ranges):
                grid[rs + r_loc][cs + c_loc] = c_extra
    return grid