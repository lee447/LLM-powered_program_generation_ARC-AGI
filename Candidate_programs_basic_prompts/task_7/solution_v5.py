def solve(grid):
    h, w = len(grid), len(grid[0])
    BACK = 4
    # find separator rows and cols
    sep_rows = [r for r in range(h) if all(grid[r][c] == BACK for c in range(w))]
    sep_cols = [c for c in range(w) if all(grid[r][c] == BACK for r in range(h))]
    row_segs = []
    prev = -1
    for r in sep_rows + [h]:
        if r - prev - 1 > 0:
            row_segs.append((prev+1, r-1))
        prev = r
    col_segs = []
    prev = -1
    for c in sep_cols + [w]:
        if c - prev - 1 > 0:
            col_segs.append((prev+1, c-1))
        prev = c
    # detect new color: first non-BACK block that has a single other color
    newc = None
    for br,(r0,r1) in enumerate(row_segs[:2]):
        for bc,(c0,c1) in enumerate(col_segs):
            cols = set()
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    v = grid[r][c]
                    if v not in (BACK,0,1):
                        cols.add(v)
            if len(cols)==1:
                newc = cols.pop()
                break
        if newc is not None:
            break
    if newc is None:
        newc = 8
    out = [row[:] for row in grid]
    # for the first two row segments only, mark the anti-diagonal of blocks
    for br in range(2):
        bc = 2 - br
        if 0 <= bc < len(col_segs):
            r0,r1 = row_segs[br]
            c0,c1 = col_segs[bc]
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    if out[r][c] == 1:
                        out[r][c] = newc
    return out