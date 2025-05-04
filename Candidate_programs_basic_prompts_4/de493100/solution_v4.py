def solve(grid):
    H, W = len(grid), len(grid[0])
    # find marker color: one that forms a solid rectangle
    from collections import Counter
    cnt = Counter(c for row in grid for c in row)
    for cand in sorted(cnt, key=lambda x: cnt[x]):
        pts = [(i,j) for i,row in enumerate(grid) for j,v in enumerate(row) if v==cand]
        if not pts: continue
        rs = [i for i,j in pts]; cs = [j for i,j in pts]
        r0,r1,minc,maxc = min(rs), max(rs), min(cs), max(cs)
        ok = True
        for i in range(r0,r1+1):
            for j in range(minc,maxc+1):
                if grid[i][j]!=cand:
                    ok=False; break
            if not ok: break
        if ok:
            # found marker rectangle
            if cand:
                # choose payload region adjacent above, left, right or below
                # prefer above
                if r0>0:
                    rs0,rs1 = r0-(r1-r0+1), r0-1
                    if rs0>=0:
                        out = [row[minc:maxc+1] for row in grid[rs0:rs1+1]]
                        return out
                # else left
                if minc>0:
                    cs0,cs1 = minc-(maxc-minc+1), minc-1
                    if cs0>=0:
                        return [row[cs0:cs1+1] for row in grid[r0:r1+1]]
                # else right
                if maxc<W-1:
                    cs0,cs1 = maxc+1, maxc*2-minc
                    if cs1<W:
                        return [row[cs0:cs1+1] for row in grid[r0:r1+1]]
                # else below
                if r1<H-1:
                    rs0,rs1 = r1+1, r1*2-r0+1
                    if rs1<H:
                        return [row[minc:maxc+1] for row in grid[rs0:rs1+1]]
    return []