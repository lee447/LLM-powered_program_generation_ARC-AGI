def solve(grid):
    nrows = len(grid)
    ncols = len(grid[0])
    row_seps = [i for i in range(nrows) if all(grid[i][j] == 3 for j in range(ncols))]
    col_seps = [j for j in range(ncols) if all(grid[i][j] == 3 for i in range(nrows))]
    row_blocks = []
    prev = -1
    for sep in row_seps:
        if sep - prev > 1:
            row_blocks.append((prev + 1, sep - 1))
        prev = sep
    if prev < nrows - 1:
        row_blocks.append((prev + 1, nrows - 1))
    col_blocks = []
    prev = -1
    for sep in col_seps:
        if sep - prev > 1:
            col_blocks.append((prev + 1, sep - 1))
        prev = sep
    if prev < ncols - 1:
        col_blocks.append((prev + 1, ncols - 1))
    out = [row[:] for row in grid]
    last_rb = len(row_blocks) - 1
    last_cb = len(col_blocks) - 1
    for i, (r0, r1) in enumerate(row_blocks):
        if i == 0:
            for j, (c0, c1) in enumerate(col_blocks):
                if j == 0:
                    color = 2
                elif j == last_cb:
                    color = 4
                else:
                    continue
                for r in range(r0, r1 + 1):
                    for c in range(c0, c1 + 1):
                        if out[r][c] == 0:
                            out[r][c] = color
        elif i == last_rb:
            for j, (c0, c1) in enumerate(col_blocks):
                if j == 0:
                    color = 1
                elif j == last_cb:
                    color = 8
                else:
                    continue
                for r in range(r0, r1 + 1):
                    for c in range(c0, c1 + 1):
                        if out[r][c] == 0:
                            out[r][c] = color
        else:
            for j in range(1, last_cb):
                c0, c1 = col_blocks[j]
                for r in range(r0, r1 + 1):
                    for c in range(c0, c1 + 1):
                        if out[r][c] == 0:
                            out[r][c] = 7
    return out