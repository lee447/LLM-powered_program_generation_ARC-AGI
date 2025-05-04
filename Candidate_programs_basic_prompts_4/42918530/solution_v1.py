def solve(grid):
    H = len(grid)
    W = len(grid[0])
    # find separator rows and cols
    sep_rows = [r for r in range(H) if all(grid[r][c] == 0 for c in range(W))]
    sep_cols = [c for c in range(W) if all(grid[r][c] == 0 for r in range(H))]
    br = len(sep_rows) - 1
    bc = len(sep_cols) - 1
    h = sep_rows[1] - sep_rows[0] - 1
    w = sep_cols[1] - sep_cols[0] - 1
    ch = h // 2
    cw = w // 2
    out = [row[:] for row in grid]
    for bi in range(br):
        for bj in range(bc):
            r0 = sep_rows[0] + bi * (h + 1) + 1
            c0 = sep_cols[0] + bj * (w + 1) + 1
            col = grid[r0][c0]
            # check if interior is all zeros
            empty = True
            for i in range(1, h-1):
                for j in range(1, w-1):
                    if grid[r0+i][c0+j] != 0:
                        empty = False
                        break
                if not empty:
                    break
            # check if this block has a twin with a nonempty interior
            twin_found = False
            for i2 in range(br):
                for j2 in range(bc):
                    if i2==bi and j2==bj: continue
                    r1 = sep_rows[0] + i2*(h+1)+1
                    c1 = sep_cols[0] + j2*(w+1)+1
                    cnt = 0
                    for di in range(1,h-1):
                        for dj in range(1,w-1):
                            if grid[r1+di][c1+dj] != 0:
                                cnt += 1
                    if cnt>0:
                        twin_found = True
            if empty and twin_found:
                for i in range(1, h-1):
                    for j in range(1, w-1):
                        if i == ch or j == cw:
                            out[r0+i][c0+j] = col
    return out