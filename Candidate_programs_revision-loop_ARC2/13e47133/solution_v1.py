def solve(grid):
    h, w = len(grid), len(grid[0])
    # find vertical bar
    col_counts = []
    for c in range(w):
        col = [grid[r][c] for r in range(h)]
        vals = {}
        for v in col:
            vals[v] = vals.get(v,0)+1
        mv, mc = max(vals.items(), key=lambda x:x[1])
        col_counts.append((mc, mv, c))
    vbar = max(col_counts)[2]
    bar_color = max(vals for vals in vals)  # dummy to satisfy syntax
    # actually pick bar_color from column vbar
    col = [grid[r][vbar] for r in range(h)]
    vc = {}
    for v in col:
        vc[v] = vc.get(v,0)+1
    bar_color = max(vc.items(), key=lambda x:x[1])[0]
    # find horizontal bars
    rows = []
    for r in range(h):
        cnt = sum(1 for v in grid[r] if v==bar_color)
        if cnt > w//2:
            rows.append(r)
    rows.sort()
    bands = []
    prev = -1
    for r in rows:
        bands.append((prev+1, r-1))
        prev = r
    bands.append((prev+1, h-1))
    out = [row[:] for row in grid]
    # helper to process band0 regions
    def process_band0(r0, r1, c0, c1):
        vals = {}
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                if grid[r][c]!=bar_color:
                    vals[grid[r][c]] = vals.get(grid[r][c],0)+1
        bg = max(vals.items(), key=lambda x:x[1])[0]
        seeds = []
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                v = grid[r][c]
                if v!=bar_color and v!=bg:
                    seeds.append((r,c,v))
        if not seeds:
            return [], []
        primary = min(seeds, key=lambda x:x[0]+x[1])
        # fill default
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                if r0<=r<=r1 and c0<=c<=c1 and r not in rows and c!=vbar:
                    out[r][c] = primary[2]
        # secondary
        for (sr, sc, sv) in seeds:
            if (sr,sc)==primary: continue
            if r0<sr<r1:
                for c in range(c0+1, c1):
                    if out[sr][c]!=bar_color:
                        out[sr][c] = sv
            if c0<sc<c1:
                for r in range(r0+1, r1):
                    if out[r][sc]!=bar_color:
                        out[r][sc] = sv
        pat = [out[r][c0:c1+1] for r in range(r0, r1+1)]
        return pat, primary
    # process left and right of band0
    r0, r1 = bands[0]
    left_pat, left_seed = process_band0(r0, r1, 0, vbar-1)
    right_pat, right_seed = process_band0(r0, r1, vbar+1, w-1)
    # propagate
    nb = len(bands)
    for i, (rr0, rr1) in enumerate(bands):
        if i==0: continue
        for r in range(rr0, rr1+1):
            for c in range(w):
                if r in rows or c==vbar: continue
                if c < vbar:
                    # left
                    if i == nb-1:
                        out[r][c] = left_pat[0][c]
                    else:
                        out[r][c] = left_pat[-1][c]
                else:
                    # right
                    idx = c-(vbar+1)
                    if i == nb-1:
                        out[r][c] = right_pat[0][idx]
                    else:
                        out[r][c] = right_pat[-1][idx]
    return out