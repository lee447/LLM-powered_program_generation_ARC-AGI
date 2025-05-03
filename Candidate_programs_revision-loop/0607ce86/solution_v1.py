def solve(grid):
    R = len(grid)
    C = len(grid[0])
    rows_nonzero = [any(grid[r][c] != 0 for c in range(C)) for r in range(R)]
    bands = []
    r = 0
    while r < R:
        if rows_nonzero[r]:
            start = r
            while r + 1 < R and rows_nonzero[r + 1]:
                r += 1
            bands.append((start, r))
        r += 1
    out = [[0]*C for _ in range(R)]
    for r0, r1 in bands:
        H = r1 - r0 + 1
        col_nonzero = [any(grid[r][c] != 0 for r in range(r0, r1+1)) for c in range(C)]
        raw_intervals = []
        c = 0
        while c < C:
            if col_nonzero[c]:
                cs = c
                while c+1 < C and col_nonzero[c+1]:
                    c += 1
                raw_intervals.append((cs, c))
            c += 1
        widths = [c1-c0+1 for c0,c1 in raw_intervals]
        counts = {}
        for w in widths:
            counts[w] = counts.get(w,0) + 1
        valid_widths = {w for w,ct in counts.items() if ct >= 2}
        valid_intervals = [(c0,c1) for (c0,c1),w in zip(raw_intervals,widths) if w in valid_widths]
        if not valid_intervals: continue
        W = valid_intervals[0][1] - valid_intervals[0][0] + 1
        P = [[0]*W for _ in range(H)]
        for c0,c1 in valid_intervals:
            for dr in range(H):
                for dc in range(W):
                    v = grid[r0+dr][c0+dc]
                    if v != 0:
                        P[dr][dc] = v
        for c0,c1 in valid_intervals:
            for dr in range(H):
                for dc in range(W):
                    out[r0+dr][c0+dc] = P[dr][dc]
    return out