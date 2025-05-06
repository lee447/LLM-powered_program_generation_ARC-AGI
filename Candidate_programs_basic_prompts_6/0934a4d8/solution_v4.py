def solve(grid):
    H=len(grid); W=len(grid[0])
    pts=[(i,j) for i in range(H) for j in range(W) if grid[i][j]==8]
    rmin=min(i for i,j in pts); rmax=max(i for i,j in pts)
    cmin=min(j for i,j in pts); cmax=max(j for i,j in pts)
    h=rmax-rmin+1; w=cmax-cmin+1
    best=None
    for ro in range(h):
        if (H-ro)%h: continue
        for co in range(w):
            if (W-co)%w: continue
            if (rmin-ro)%h or (cmin-co)%w: continue
            R=(H-ro)//h; C=(W-co)//w
            blanks=0
            for ti in range(R):
                for tj in range(C):
                    si=ro+ti*h; sj=co+tj*w
                    ok=True
                    for i in range(si,si+h):
                        for j in range(sj,sj+w):
                            if grid[i][j]!=8:
                                ok=False; break
                        if not ok: break
                    if ok: blanks+=1
            if blanks==1:
                best=(ro,co,R,C); break
        if best: break
    ro,co,R,C=best
    bi=(rmin-ro)//h; bj=(cmin-co)//w
    tiles=[]
    for ti in range(R):
        for tj in range(C):
            if ti==bi and tj==bj: continue
            si=ro+ti*h; sj=co+tj*w
            mat=[tuple(grid[i][sj:sj+w]) for i in range(si,si+h)]
            if any(8 in row for row in mat): continue
            tiles.append((ti,tj,mat))
    nbr={}
    if bi>0:
        ti,tj=bi-1,bj; si=ro+ti*h; sj=co+tj*w
        nbr['top']=[grid[si+h-1][sj+x] for x in range(w)]
    if bi<R-1:
        ti,tj=bi+1,bj; si=ro+ti*h; sj=co+tj*w
        nbr['bottom']=[grid[si][sj+x] for x in range(w)]
    if bj>0:
        ti,tj=bi,bj-1; si=ro+ti*h; sj=co+tj*w
        nbr['left']=[grid[si+x][sj+w-1] for x in range(h)]
    if bj<C-1:
        ti,tj=bi,bj+1; si=ro+ti*h; sj=co+tj*w
        nbr['right']=[grid[si+x][sj] for x in range(h)]
    for _,_,mat in tiles:
        ok=True
        for side,arr in nbr.items():
            if side=='top' and list(mat[0])!=arr: ok=False; break
            if side=='bottom' and list(mat[-1])!=arr: ok=False; break
            if side=='left' and [row[0] for row in mat]!=arr: ok=False; break
            if side=='right' and [row[-1] for row in mat]!=arr: ok=False; break
        if ok:
            return [list(row) for row in mat]
    return []