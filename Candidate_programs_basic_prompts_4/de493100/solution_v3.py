def solve(grid):
    H, W = len(grid), len(grid[0])
    drow = [sum(grid[i][j]!=grid[i+1][j] for j in range(W)) for i in range(H-1)]
    dcol = [sum(grid[i][j]!=grid[i][j+1] for i in range(H)) for j in range(W-1)]
    thr_r = max(drow)*0.5
    thr_c = max(dcol)*0.5
    rb, cb = [-1], [-1]
    for i, v in enumerate(drow):
        if v >= thr_r: rb.append(i)
    for j, v in enumerate(dcol):
        if v >= thr_c: cb.append(j)
    rb.append(H-1)
    cb.append(W-1)
    rows = [(rb[i]+1, rb[i+1]) for i in range(len(rb)-1)]
    cols = [(cb[i]+1, cb[i+1]) for i in range(len(cb)-1)]
    out = []
    for r0, r1 in rows:
        row = []
        for c0, c1 in cols:
            freq = {}
            for i in range(r0, r1+1):
                for j in range(c0, c1+1):
                    freq[grid[i][j]] = freq.get(grid[i][j], 0) + 1
            val = max(freq, key=lambda k: freq[k])
            row.append(val)
        out.append(row)
    return out