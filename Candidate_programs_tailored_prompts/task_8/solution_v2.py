def solve(grid):
    H = len(grid)
    W = len(grid[0])
    sep_rows = [i for i in range(H) if all(c == 0 for c in grid[i])]
    sep_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    res = [row[:] for row in grid]
    for bi in range(len(sep_rows) - 1):
        r0 = sep_rows[bi] + 1
        r1 = sep_rows[bi + 1]
        for bj in range(len(sep_cols) - 1):
            c0 = sep_cols[bj] + 1
            c1 = sep_cols[bj + 1]
            R = range(r0, r1)
            C = range(c0, c1)
            colors = {grid[i][j] for i in R for j in C if grid[i][j] != 0}
            if len(colors) != 2:
                continue
            a, b = colors
            rf, rl = r0, r1 - 1
            cf, cl = c0, c1 - 1
            Lpos = {
                (rf, cf), (rf, cf + 1), (rf + 1, cf),
                (rf, cl), (rf, cl - 1), (rf + 1, cl),
                (rl, cf), (rl, cf + 1), (rl - 1, cf),
                (rl, cl), (rl, cl - 1), (rl - 1, cl)
            }
            cnta = sum(1 for (i, j) in Lpos if grid[i][j] == a)
            cntb = sum(1 for (i, j) in Lpos if grid[i][j] == b)
            if cnta > cntb:
                Lc, Fc = a, b
            else:
                Lc, Fc = b, a
            if (bi + bj) % 2 == 0:
                Lc, Fc = Fc, Lc
            for i in R:
                for j in C:
                    res[i][j] = Lc if (i, j) in Lpos else Fc
    return res