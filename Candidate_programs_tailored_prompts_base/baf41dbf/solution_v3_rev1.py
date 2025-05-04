def solve(grid):
    h=len(grid); w=len(grid[0])
    anchors=[]
    rmin0=rmax0=cmin0=cmax0=None
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3:
                if rmin0 is None:
                    rmin0=rmax0=i; cmin0=cmax0=j
                else:
                    rmin0=min(rmin0,i); rmax0=max(rmax0,i)
                    cmin0=min(cmin0,j); cmax0=max(cmax0,j)
            elif grid[i][j]==6:
                anchors.append((i,j))
    nrmin,nrmax,ncmin,ncmax=rmin0,rmax0,cmin0,cmax0
    for r,c in anchors:
        if r<rmin0: nrmin=min(nrmin,r+1)
        if r>rmax0: nrmax=max(nrmax,r-1)
        if c<cmin0: ncmin=min(ncmin,c+1)
        if c>cmax0: ncmax=max(ncmax,c-1)
    interior_rows=[]
    for i in range(rmin0+1,rmax0):
        ok=True
        for j in range(cmin0,cmax0+1):
            if grid[i][j]!=3:
                ok=False; break
        if ok: interior_rows.append(i)
    interior_cols=[]
    for j in range(cmin0+1,cmax0):
        ok=True
        for i in range(rmin0,rmax0+1):
            if grid[i][j]!=3:
                ok=False; break
        if ok: interior_cols.append(j)
    out=[[0]*w for _ in range(h)]
    for j in range(ncmin,ncmax+1):
        out[nrmin][j]=3; out[nrmax][j]=3
    for i in range(nrmin,nrmax+1):
        out[i][ncmin]=3; out[i][ncmax]=3
    for i in interior_rows:
        for j in range(ncmin,ncmax+1):
            out[i][j]=3
    for j in interior_cols:
        for i in range(nrmin,nrmax+1):
            out[i][j]=3
    for r,c in anchors:
        out[r][c]=6
    return out