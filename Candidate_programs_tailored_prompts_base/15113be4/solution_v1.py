def solve(grid):
    R, C = len(grid), len(grid[0])
    sep_r = [r for r in range(R) if all(grid[r][c] == 4 for c in range(C))]
    sep_c = [c for c in range(C) if all(grid[r][c] == 4 for r in range(R))]
    row_segs = []
    prev = -1
    for r in sep_r + [R]:
        if r - prev - 1 > 0:
            row_segs.append(list(range(prev + 1, r)))
        prev = r
    col_segs = []
    prev = -1
    for c in sep_c + [C]:
        if c - prev - 1 > 0:
            col_segs.append(list(range(prev + 1, c)))
        prev = c
    src = None
    for seg in row_segs:
        for cseg in col_segs:
            for r in seg:
                if r + 1 in seg:
                    for c in cseg:
                        if c + 1 in cseg:
                            v = grid[r][c]
                            if v > 1 and grid[r][c+1] == v and grid[r+1][c] == v and grid[r+1][c+1] == v:
                                dr0, dc0 = r - seg[0], c - cseg[0]
                                dr1, dc1 = dr0 + 1, dc0 + 1
                                src = (v, dr0, dc0, dr1, dc1)
                                break
                    if src: break
            if src: break
        if src: break
    v, dr0, dc0, dr1, dc1 = src
    out = [row[:] for row in grid]
    for seg in row_segs:
        for cseg in col_segs:
            r0, c0 = seg[0], cseg[0]
            out[r0+dr0][c0+dc0] = v
            out[r0+dr1][c0+dc1] = v
    return out