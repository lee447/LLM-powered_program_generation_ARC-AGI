def solve(grid):
    h, w = len(grid), len(grid[0])
    counts = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v:
                counts[v] = counts.get(v, 0) + 1
    shape_col = max(counts, key=lambda k: counts[k])
    pts = [(r,c) for r in range(h) for c in range(w) if grid[r][c]==shape_col]
    minr = min(r for r,c in pts)
    maxr = max(r for r,c in pts)
    minc = min(c for r,c in pts)
    maxc = max(c for r,c in pts)
    H = maxr - minr + 1
    W = maxc - minc + 1
    tpl = [[0]*W for _ in range(H)]
    for r,c in pts:
        tpl[r-minr][c-minc] = 1
    markers = [(r,c,clr) for clr,(cnt) in counts.items() if clr!=shape_col and cnt==1 for r in range(h) for c in range(w) if grid[r][c]==clr]
    out = [row[:] for row in grid]
    for mr,mc,clr in markers:
        flip_h = mc > maxc
        flip_v = mr > maxr
        t = [row[:] for row in tpl]
        if flip_h:
            t = [row[::-1] for row in t]
        if flip_v:
            t = t[::-1]
        pr = H//2
        pc = W//2
        dr = mr - pr
        dc = mc - pc
        for r in range(H):
            for c in range(W):
                if t[r][c]:
                    rr, cc = dr+r, dc+c
                    if 0 <= rr < h and 0 <= cc < w:
                        out[rr][cc] = clr
    return out