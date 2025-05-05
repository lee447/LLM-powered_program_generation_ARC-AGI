def solve(grid):
    h, w = len(grid), len(grid[0])
    hr = [r for r in range(h) if all(grid[r][c] == 3 for c in range(w))]
    vc = [c for c in range(w) if all(grid[r][c] == 3 for r in range(h))]
    rsegs, prev = [], -1
    for r in hr:
        rsegs.append((prev+1, r))
        prev = r
    rsegs.append((prev+1, h))
    csegs, prev = [], -1
    for c in vc:
        csegs.append((prev+1, c))
        prev = c
    csegs.append((prev+1, w))
    out = [row[:] for row in grid]
    nr, nc = len(rsegs), len(csegs)
    # top row
    r0, r1 = rsegs[0]
    c0, c1 = csegs[0]
    for r in range(r0, r1):
        for c in range(c0, c1):
            out[r][c] = 2
    c0, c1 = csegs[-1]
    for r in range(r0, r1):
        for c in range(c0, c1):
            out[r][c] = 4
    # interior
    for i in range(1, nr-1):
        r0, r1 = rsegs[i]
        for j in range(1, nc-1):
            c0, c1 = csegs[j]
            for r in range(r0, r1):
                for c in range(c0, c1):
                    out[r][c] = 7
    # bottom row
    r0, r1 = rsegs[-1]
    c0, c1 = csegs[0]
    for r in range(r0, r1):
        for c in range(c0, c1):
            out[r][c] = 1
    c0, c1 = csegs[-1]
    for r in range(r0, r1):
        for c in range(c0, c1):
            out[r][c] = 8
    return out