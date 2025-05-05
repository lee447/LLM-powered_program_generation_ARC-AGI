def solve(grid):
    H, W = len(grid), len(grid[0])
    sep_rows = [r for r in range(H) if sum(1 for c in range(W) if grid[r][c]==7) > W//2]
    sep_cols = [c for c in range(W) if sum(1 for r in range(H) if grid[r][c]==7) > H//2]
    rows = [-1] + sep_rows + [H]
    cols = [-1] + sep_cols + [W]
    def period2d(sub):
        h, w = len(sub), len(sub[0])
        ph = h
        for p in range(1, h+1):
            if h%p: continue
            ok = True
            for i in range(h-p):
                for j in range(w):
                    if sub[i][j] != sub[i+p][j]:
                        ok = False; break
                if not ok: break
            if ok:
                ph = p; break
        pw = w
        for p in range(1, w+1):
            if w%p: continue
            ok = True
            for j in range(w-p):
                for i in range(h):
                    if sub[i][j] != sub[i][j+p]:
                        ok = False; break
                if not ok: break
            if ok:
                pw = p; break
        return ph, pw
    for i in range(len(rows)-1):
        for j in range(len(cols)-1):
            r0, r1 = rows[i]+1, rows[i+1]
            c0, c1 = cols[j]+1, cols[j+1]
            if r1<=r0 or c1<=c0: continue
            sub = [row[c0:c1] for row in grid[r0:r1]]
            vals = set(v for row in sub for v in row if v!=7)
            if len(vals) > 2:
                ph, pw = period2d(sub)
                return [row[:pw] for row in sub[:ph]]
    return []