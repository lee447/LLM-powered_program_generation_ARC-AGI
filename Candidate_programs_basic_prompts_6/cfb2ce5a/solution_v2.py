def solve(grid):
    h=len(grid); w=len(grid[0])
    nz_rows=[i for i in range(h) if any(grid[i][j]!=0 for j in range(w))]
    nz_cols=[j for j in range(w) if any(grid[i][j]!=0 for i in range(h))]
    rmin,rmax=min(nz_rows),max(nz_rows)
    cmin,cmax=min(nz_cols),max(nz_cols)
    inner_h=rmax-rmin+1; inner_w=cmax-cmin+1
    rh=inner_h//2; cw=inner_w//2
    row_segs=[(rmin,rmin+rh-1),(rmin+rh,rmax)]
    col_segs=[(cmin,cmin+cw-1),(cmin+cw,cmax)]
    def subblock(r0,c0,r1,c1):
        return [row[c0:c1+1] for row in grid[r0:r1+1]]
    TLr0,TLr1=row_segs[0][0],row_segs[0][1]
    TLc0,TLc1=col_segs[0][0],col_segs[0][1]
    base=[[grid[i][j] for j in range(TLc0,TLc1+1)] for i in range(TLr0,TLr1+1)]
    base_keys=sorted({v for row in base for v in row if v!=0})
    def rot90(m):
        return [list(reversed(col)) for col in zip(*m)]
    def rot180(m):
        return [list(reversed(row)) for row in reversed(m)]
    def rot270(m):
        return [list(col) for col in reversed(list(zip(*m)))]
    def flipH(m):
        return [list(reversed(row)) for row in m]
    def flipV(m):
        return list(reversed(m))
    transforms=[lambda m:m, rot90, rot180, rot270, flipH, flipV]
    out=[row[:] for row in grid]
    for qi in (0,1):
        for qj in (0,1):
            if qi==0 and qj==0: continue
            r0,c0=row_segs[qi][0],col_segs[qj][0]
            r1,c1=row_segs[qi][1],col_segs[qj][1]
            seeds=sorted({grid[i][j] for i in range(r0,r1+1) for j in range(c0,c1+1) if grid[i][j]!=0})
            if not seeds: continue
            blk_h=r1-r0+1; blk_w=c1-c0+1
            for tf in transforms:
                cand=tf(base)
                if len(cand)!=blk_h or len(cand[0])!=blk_w: continue
                for direct in (True,False):
                    mp={}
                    ok=True
                    for k,val in enumerate(base_keys):
                        sv=seeds[k] if direct else seeds[-1-k]
                        mp[val]=sv
                    for i in range(blk_h):
                        for j in range(blk_w):
                            iv=grid[r0+i][c0+j]
                            if iv!=0 and mp.get(cand[i][j],None)!=iv:
                                ok=False; break
                        if not ok: break
                    if ok:
                        for i in range(blk_h):
                            for j in range(blk_w):
                                out[r0+i][c0+j]=mp.get(cand[i][j],0)
                        tf=transforms[-1]  # break outer
                        break
                if ok: break
    return out