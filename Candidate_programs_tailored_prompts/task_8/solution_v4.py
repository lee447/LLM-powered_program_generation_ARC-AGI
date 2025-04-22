def solve(grid):
    rows = len(grid)
    cols = len(grid[0])
    # find separator rows and cols
    row_seps = [r for r in range(rows) if all(grid[r][c] == 0 for c in range(cols))]
    col_seps = [c for c in range(cols) if all(grid[r][c] == 0 for r in range(rows))]
    # make a copy
    out = [row[:] for row in grid]
    # interior segments
    rsegs = [(row_seps[i]+1, row_seps[i+1]-1) for i in range(len(row_seps)-1)]
    csegs = [(col_seps[i]+1, col_seps[i+1]-1) for i in range(len(col_seps)-1)]
    for bi, (r0, r1) in enumerate(rsegs):
        for bj, (c0, c1) in enumerate(csegs):
            # gather nonzero colors
            cols_in_block = set()
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    v = grid[r][c]
                    if v != 0:
                        cols_in_block.add(v)
            if len(cols_in_block) != 2:
                continue
            a, b = cols_in_block
            # detect which color is at the block's top-left corner
            orig_L = grid[r0][c0]
            if orig_L not in cols_in_block:
                orig_L = a
            orig_fill = a if orig_L == b else b
            # if even sum of block coords, swap roles
            swap = ((bi + bj) % 2 == 0)
            Lc = orig_fill if swap else orig_L
            Fc = orig_L if swap else orig_fill
            m = r1 - r0 + 1
            arms = m - 2
            for r in range(r0, r1+1):
                for c in range(c0, c1+1):
                    if grid[r][c] == 0:
                        continue
                    # L shape at top-left
                    if (r - r0 < arms and c == c0) or (c - c0 < arms and r == r0):
                        out[r][c] = Lc
                    else:
                        out[r][c] = Fc
    return out