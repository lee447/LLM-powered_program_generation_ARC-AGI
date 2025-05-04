def solve(grid):
    H, W = len(grid), len(grid[0])
    zero_rows = [i for i in range(H) if all(v == 0 for v in grid[i])]
    zero_cols = [j for j in range(W) if all(grid[i][j] == 0 for i in range(H))]
    zr, zc = zero_rows, zero_cols
    row_intervals = []
    for i in range(len(zr)-1):
        if zr[i+1] - zr[i] > 1:
            row_intervals.append(list(range(zr[i]+1, zr[i+1])))
    col_intervals = []
    for j in range(len(zc)-1):
        if zc[j+1] - zc[j] > 1:
            col_intervals.append(list(range(zc[j]+1, zc[j+1])))
    R, C = len(row_intervals), len(col_intervals)
    out = [row[:] for row in grid]
    for bi in range(R):
        rs = row_intervals[bi]
        for bj in range(C):
            cs = col_intervals[bj]
            cnt = {}
            for r in rs:
                for c in cs:
                    v = grid[r][c]
                    if v:
                        cnt[v] = cnt.get(v, 0) + 1
            if len(cnt) != 2:
                continue
            items = sorted(cnt.items(), key=lambda x: x[1])
            sec, prv = items[0][0], items[1][0]
            coords = [(r, c) for r in rs for c in cs if grid[r][c] == sec]
            lrs = [r - rs[0] for r, c in coords]
            lcs = [c - cs[0] for r, c in coords]
            minr, maxr = min(lrs), max(lrs)
            minc, maxc = min(lcs), max(lcs)
            shape = [(lr - minr, lc - minc) for lr, lc in zip(lrs, lcs)]
            h_bb = maxr - minr + 1
            w_bb = maxc - minc + 1
            for r, c in coords:
                out[r][c] = prv
            bh = len(rs)
            bw = len(cs)
            denom_r = max(R-1,1)
            denom_c = max(C-1,1)
            r_off = int((bh - h_bb) * bi / denom_r + 0.5)
            c_off = int((bw - w_bb) * bj / denom_c + 0.5)
            for dr, dc in shape:
                out[rs[0] + r_off + dr][cs[0] + c_off + dc] = sec
    return out