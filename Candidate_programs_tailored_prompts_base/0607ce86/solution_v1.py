def solve(grid):
    n = len(grid)
    m = len(grid[0])
    nzr = [sum(1 for x in row if x != 0) for row in grid]
    max_nzr = max(nzr)
    # find core columns
    col_nz = [sum(1 for i in range(n) if grid[i][j] != 0) for j in range(m)]
    thr_c = max(col_nz) // 2
    core_cols = [j for j, c in enumerate(col_nz) if c > thr_c]
    thr_r = len(core_cols) // 2
    band_rows = [i for i in range(n) if sum(1 for j in core_cols if grid[i][j] != 0) > thr_r]
    band_rows.sort()
    segs = []
    for i in band_rows:
        if not segs or i != segs[-1][-1] + 1:
            segs.append([i])
        else:
            segs[-1].append(i)
    lengths = {}
    for s in segs:
        lengths[len(s)] = lengths.get(len(s), 0) + 1
    if not lengths:
        return [[0]*m for _ in range(n)]
    H = max(lengths, key=lambda k: lengths[k])
    bands = [s for s in segs if len(s) == H]
    if not bands:
        return [[0]*m for _ in range(n)]
    # compute canonical rows
    canonical = []
    for k in range(H):
        row = []
        for j in range(m):
            cnt = {}
            for s in bands:
                v = grid[s[0] + k][j]
                cnt[v] = cnt.get(v, 0) + 1
            # pick mode, tie -> larger value
            best = max(cnt.items(), key=lambda x: (x[1], x[0]))[0]
            row.append(best)
        canonical.append(row)
    out = [[0]*m for _ in range(n)]
    for s in bands:
        for k in range(H):
            out[s[0] + k] = canonical[k][:]
    return out