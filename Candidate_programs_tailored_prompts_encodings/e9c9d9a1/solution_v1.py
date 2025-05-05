def solve(grid):
    h, w = len(grid), len(grid[0])
    hseps = [r for r in range(h) if all(grid[r][c] == 3 for c in range(w))]
    vseps = [c for c in range(w) if all(grid[r][c] == 3 for r in range(h))]
    row_intervals = []
    prev = -1
    for r in sorted(hseps):
        if prev + 1 < r:
            row_intervals.append((prev + 1, r))
        prev = r
    if prev + 1 < h:
        row_intervals.append((prev + 1, h))
    col_intervals = []
    prev = -1
    for c in sorted(vseps):
        if prev + 1 < c:
            col_intervals.append((prev + 1, c))
        prev = c
    if prev + 1 < w:
        col_intervals.append((prev + 1, w))
    out = [row[:] for row in grid]
    rn, cn = len(row_intervals), len(col_intervals)
    if rn and cn:
        r0, r1 = row_intervals[0]
        c0, c1 = col_intervals[0]
        for rr in range(r0, r1):
            for cc in range(c0, c1):
                out[rr][cc] = 2
        r0, r1 = row_intervals[0]
        c0, c1 = col_intervals[cn - 1]
        for rr in range(r0, r1):
            for cc in range(c0, c1):
                out[rr][cc] = 4
    for ri in range(1, rn - 1):
        r0, r1 = row_intervals[ri]
        for ci in range(1, cn - 1):
            c0, c1 = col_intervals[ci]
            for rr in range(r0, r1):
                for cc in range(c0, c1):
                    out[rr][cc] = 7
    if rn:
        r0, r1 = row_intervals[rn - 1]
        c0, c1 = col_intervals[0]
        for rr in range(r0, r1):
            for cc in range(c0, c1):
                out[rr][cc] = 1
        c0, c1 = col_intervals[cn - 1]
        for rr in range(r0, r1):
            for cc in range(c0, c1):
                out[rr][cc] = 8
    return out