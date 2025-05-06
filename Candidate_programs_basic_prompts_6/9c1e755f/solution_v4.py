def solve(grid):
    orig = [row[:] for row in grid]
    out = [row[:] for row in grid]
    h_axes = {}
    for i,row in enumerate(orig):
        cols = [j for j,v in enumerate(row) if v!=0]
        if len(cols)>=2:
            h_axes[i] = cols
    v_axes = {}
    w = len(orig[0])
    h = len(orig)
    for j in range(w):
        rows = [i for i in range(h) if orig[i][j]!=0]
        if len(rows)>=2:
            v_axes[j] = rows
    # H-groups: fill using horizontal patterns along each vertical axis
    for c, vrows in v_axes.items():
        hrows = [r for r,cols in h_axes.items() if c in cols]
        if not hrows:
            continue
        cols_union = sorted({j for r in hrows for j in h_axes[r]})
        colors = {orig[r][j] for r in hrows for j in h_axes[r]}
        if len(colors)<=1:
            continue
        r0 = min(hrows)
        for i in vrows:
            if i in hrows:
                continue
            for j in cols_union:
                if j==c or orig[i][j]!=0:
                    continue
                idx = (i - r0) % len(hrows)
                pr = hrows[idx]
                out[i][j] = orig[pr][j]
    # V-groups: fill using vertical patterns along each horizontal axis
    for r, hcols in h_axes.items():
        vcols = [c for c, vrows in v_axes.items() if r in vrows]
        if not vcols:
            continue
        rows_union = sorted({i for c in vcols for i in v_axes[c]})
        colors = {orig[i][c] for c in vcols for i in v_axes[c]}
        if len(colors)<=1:
            continue
        c0 = min(vcols)
        for j in hcols:
            if j in vcols:
                continue
            for i in rows_union:
                if i==r or orig[i][j]!=0:
                    continue
                idx = (j - c0) % len(vcols)
                pc = vcols[idx]
                out[i][j] = orig[i][pc]
    return out