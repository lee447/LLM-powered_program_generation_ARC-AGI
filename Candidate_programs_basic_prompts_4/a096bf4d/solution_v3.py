def solve(grid):
    R, C = len(grid), len(grid[0])
    row_active = [any(grid[r][c] != 0 for c in range(C)) for r in range(R)]
    row_segs = []
    r = 0
    while r < R:
        if row_active[r]:
            start = r
            while r < R and row_active[r]:
                r += 1
            row_segs.append(list(range(start, r)))
        else:
            r += 1
    col_active = [any(grid[r][c] != 0 for r in range(R)) for c in range(C)]
    col_segs = []
    c = 0
    while c < C:
        if col_active[c]:
            start = c
            while c < C and col_active[c]:
                c += 1
            col_segs.append(list(range(start, c)))
        else:
            c += 1
    bh = len(row_segs[0])
    # find special in block row 0
    br0 = row_segs[0]
    special = None
    bj = None
    dr = dc = None
    for j, cs in enumerate(col_segs):
        # gather counts
        cnt = {}
        for r in br0:
            for c in cs:
                v = grid[r][c]
                cnt[v] = cnt.get(v, 0) + 1
        singles = [v for v, k in cnt.items() if k == 1 and v != 0]
        if len(singles) == 1:
            special = singles[0]
            bj = j
            # find its position
            for r in br0:
                for c in cs:
                    if grid[r][c] == special:
                        dr = r - br0[0]
                        dc = c - cs[0]
                        break
                if dr is not None:
                    break
            break
    if special is None:
        return grid
    # propagate
    for i, rs in enumerate(row_segs):
        if i == 0 or len(rs) != bh:
            continue
        cc = col_segs[bj]
        rr0 = rs[0] + dr
        cc0 = cc[0] + dc
        grid[rr0][cc0] = special
    return grid