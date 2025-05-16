def solve(grid):
    h, w = len(grid), len(grid[0])
    rects = {}
    for r in range(h):
        for c in range(w):
            f = grid[r][c]
            if f == grid[r-1][c] if r>0 else False: continue
            if f == grid[r][c-1] if c>0 else False: continue
            # try find rectangle with top-left (r,c)
            ce = c
            while ce+1<w and grid[r][ce+1]==f: ce+=1
            re = r
            while re+1<h and grid[re+1][c]==f: re+=1
            if ce-c<1 or re-r<1: continue
            ok = True
            for cc in range(c,ce+1):
                if grid[r][cc]!=f or grid[re][cc]!=f: ok=False; break
            for rr in range(r,re+1):
                if grid[rr][c]!=f or grid[rr][ce]!=f: ok=False; break
            if not ok: continue
            # check interior has any non-f
            has_interior = False
            for rr in range(r+1,re):
                for cc in range(c+1,ce):
                    if grid[rr][cc]!=f: has_interior=True; break
                if has_interior: break
            if not has_interior: continue
            rects.setdefault(f,[]).append((r,re,c,ce))
    patterns = {}
    for f,rs in rects.items():
        rs.sort(key=lambda x:(x[1]-x[0])*(x[3]-x[2]))
        r0,re0,c0,ce0 = rs[0]
        pat = [row[c0+1:ce0] for row in grid[r0+1:re0]]
        patterns[f] = (pat, re0-r0-1, ce0-c0-1)
    out = [row[:] for row in grid]
    for f,rs in rects.items():
        if f not in patterns: continue
        pat, ph, pw = patterns[f]
        for r0,re0,c0,ce0 in rs[1:]:
            H = re0-r0-1; W = ce0-c0-1
            sr = r0+1 + (H-ph)//2
            sc = c0+1 + (W-pw)//2
            for i in range(ph):
                for j in range(pw):
                    if pat[i][j]!=f:
                        out[sr+i][sc+j] = pat[i][j]
    return out