def solve(grid):
    h, w = len(grid), len(grid[0])
    cols = {}
    for i in range(h):
        for j in range(w):
            v = grid[i][j]
            if v:
                cols.setdefault(v, []).append((i, j))
    main = max((c for c in cols if len(cols[c])>1), key=lambda c: len(cols[c]))
    pts = cols[main]
    minr = min(r for r,_ in pts)
    maxr = max(r for r,_ in pts)
    minc = min(c for _,c in pts)
    maxc = max(c for _,c in pts)
    ref = sorted([(r-minr, c-minc) for r,c in pts])
    cr = (minr+maxr)/2
    cc = (minc+maxc)/2
    out = [row[:] for row in grid]
    for col, cells in cols.items():
        if col==main: continue
        ar, ac = cells[0]
        dr = ar - minr
        dc = ac - minc
        vr = abs(ar-cr)>abs(ac-cc)
        new = []
        if vr:
            H = maxr-minr+1
            for r,c in ref:
                nr = H-1-r
                new.append((nr, c))
        else:
            W = maxc-minc+1
            for r,c in ref:
                nc = W-1-c
                new.append((r, nc))
        best = None
        for nr, nc in new:
            ddr = ar-nr
            ddc = ac-nc
            cand = [(r+ddr,c+ddc) for r,c in new]
            if (ar,ac) in cand:
                best = cand
                break
        for r,c in best or []:
            if 0<=r<h and 0<=c<w:
                out[r][c] = col
    return out