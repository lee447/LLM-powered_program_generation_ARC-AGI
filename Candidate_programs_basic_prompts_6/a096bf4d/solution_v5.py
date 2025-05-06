def solve(grid):
    R, C = len(grid), len(grid[0])
    border_rows = [i for i in range(R) if all(v == 0 for v in grid[i])]
    border_cols = [j for j in range(C) if all(grid[i][j] == 0 for i in range(R))]
    block_row_tops = []
    block_height = 0
    for k in range(len(border_rows) - 1):
        r0, r1 = border_rows[k], border_rows[k+1]
        if r1 - r0 > 1:
            block_row_tops.append(r0 + 1)
            block_height = r1 - r0 - 1
    block_col_lefts = []
    block_width = 0
    for k in range(len(border_cols) - 1):
        c0, c1 = border_cols[k], border_cols[k+1]
        if c1 - c0 > 1:
            block_col_lefts.append(c0 + 1)
            block_width = c1 - c0 - 1
    B = len(block_row_tops)
    if B == 4:
        pi, pj = block_height // 2, block_width // 2
        pc = grid[block_row_tops[0] + pi][block_col_lefts[0] + pj]
        for br in block_row_tops:
            for bc in block_col_lefts:
                grid[br + pi][bc + pj] = pc
    elif B == 5:
        pi, pj = block_height // 2, block_width // 2 - 1
        pc = grid[block_row_tops[0] + pi][block_col_lefts[0] + pj]
        for br in block_row_tops:
            for bc in block_col_lefts:
                grid[br + pi][bc + pj] = pc
    else:
        for br in block_row_tops:
            for bc in block_col_lefts:
                bg = grid[br][bc]
                cnt = {}
                for di in (1, 2):
                    for dj in (1, 2):
                        v = grid[br + di][bc + dj]
                        if v != bg:
                            cnt[v] = cnt.get(v, 0) + 1
                base = None
                ptr = None
                for v, c in cnt.items():
                    if c > 1:
                        base = v
                    elif c == 1:
                        ptr = v
                if ptr is None:
                    continue
                pi = pj = None
                for di in (1, 2):
                    for dj in (1, 2):
                        if grid[br + di][bc + dj] == ptr:
                            pi, pj = di, dj
                            break
                    if pi is not None:
                        break
                mi, mj = 3 - pi, 3 - pj
                grid[br + mi][bc + mj] = base
    return grid