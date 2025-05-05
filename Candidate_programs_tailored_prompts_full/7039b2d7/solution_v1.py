def solve(grid):
    from collections import Counter
    H, W = len(grid), len(grid[0])
    cnt = Counter()
    for row in grid:
        cnt.update(row)
    bg = cnt.most_common(1)[0][0]
    stripe_rows_all = [i for i in range(H) if len(set(grid[i]))==1 and grid[i][0]!=bg]
    stripe_cols_all = [j for j in range(W) if len({grid[i][j] for i in range(H)})==1 and grid[0][j]!=bg]
    stripe_rows = [i for i in stripe_rows_all if 0<i<H-1]
    stripe_cols = [j for j in stripe_cols_all if 0<j<W-1]
    stripe_rows.sort()
    stripe_cols.sort()
    row_bounds = [-1] + stripe_rows + [H]
    col_bounds = [-1] + stripe_cols + [W]
    R, C = len(stripe_rows)+1, len(stripe_cols)+1
    sr_set = set(stripe_rows_all)
    sc_set = set(stripe_cols_all)
    res = [[0]*C for _ in range(R)]
    for r in range(R):
        r0, r1 = row_bounds[r]+1, row_bounds[r+1]
        for i in range(r0, r1):
            if i not in sr_set:
                rr = i
                break
        for c in range(C):
            c0, c1 = col_bounds[c]+1, col_bounds[c+1]
            for j in range(c0, c1):
                if j not in sc_set:
                    cc = j
                    break
            res[r][c] = grid[rr][cc]
    return res