def solve(grid):
    H, W = len(grid), len(grid[0])
    col_counts = [sum(grid[r][c] != 0 for r in range(H)) for c in range(W)]
    maxc = max(col_counts)
    if maxc == 0:
        return [[0]*W for _ in range(H)]
    threshc = maxc * 0.5
    seg_cols = [c for c in range(W) if col_counts[c] >= threshc]
    seg_cols.sort()
    segments = []
    for c in seg_cols:
        if not segments or c - segments[-1][1] > 1:
            segments.append([c, c])
        else:
            segments[-1][1] = c
    segments = [(s, e+1) for s,e in segments]
    col_in_seg = set(c for s,e in segments for c in range(s,e))
    row_counts = [sum(grid[r][c] != 0 for c in col_in_seg) for r in range(H)]
    maxr = max(row_counts)
    threshr = maxr * 0.5
    seg_rows = [r for r in range(H) if row_counts[r] >= threshr]
    seg_rows.sort()
    bands = []
    for r in seg_rows:
        if not bands or r - bands[-1][1] > 1:
            bands.append([r, r])
        else:
            bands[-1][1] = r
    bands = [(s, e+1) for s,e in bands]
    def is_stripe(r):
        for xs,xe in segments:
            v = grid[r][xs]
            if v == 0: return False
            for c in range(xs, xe):
                if grid[r][c] != v:
                    return False
        return True
    rects = []
    for ys,ye in bands:
        stripe_rows = [r for r in range(ys,ye) if is_stripe(r)]
        block_rows = [r for r in range(ys,ye) if r not in stripe_rows]
        # stripe rects
        for r in stripe_rows:
            for xs,xe in segments:
                rects.append((r, xs, 1, xe-xs))
        # block subbands
        block_rows.sort()
        runs = []
        for r in block_rows:
            if not runs or r - runs[-1][1] > 1:
                runs.append([r, r])
            else:
                runs[-1][1] = r
        for s,e in runs:
            h = e - s + 1
            for xs,xe in segments:
                # check non-zero presence
                has = any(grid[r][c] != 0 for r in range(s, e+1) for c in range(xs, xe))
                if has:
                    rects.append((s, xs, h, xe-xs))
    # group by height
    by_h = {}
    for y0,x0,h,w in rects:
        by_h.setdefault(h, []).append((y0,x0,w))
    prototypes = {}
    for h, lst in by_h.items():
        w = lst[0][2]
        p = [[0]*w for _ in range(h)]
        for dy in range(h):
            for dx in range(w):
                cnt = {}
                for y0,x0,_ in lst:
                    v = grid[y0+dy][x0+dx]
                    cnt[v] = cnt.get(v, 0) + 1
                pv = max(cnt.items(), key=lambda x: x[1])[0]
                p[dy][dx] = pv
        prototypes[h] = p
    new = [[0]*W for _ in range(H)]
    for y0,x0,h,w in rects:
        p = prototypes[h]
        for dy in range(h):
            for dx in range(w):
                new[y0+dy][x0+dx] = p[dy][dx]
    return new