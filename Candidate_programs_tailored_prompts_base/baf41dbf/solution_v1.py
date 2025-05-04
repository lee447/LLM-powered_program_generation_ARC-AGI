def solve(grid):
    h=len(grid); w=len(grid[0])
    rmin=rmax=cmin=cmax=None
    anchors=[]
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v==3:
                if rmin is None:
                    rmin=rmax=i; cmin=cmax=j
                else:
                    rmin=min(rmin,i); rmax=max(rmax,i)
                    cmin=min(cmin,j); cmax=max(cmax,j)
            elif v==6:
                anchors.append((i,j))
    nrmin,nrmax,ncmin,ncmax=rmin,rmax,cmin,cmax
    for r,c in anchors:
        if r<rmin: nrmin=min(nrmin,r+1)
        if r>rmax: nrmax=max(nrmax,r-1)
        if c<cmin: ncmin=min(ncmin,c+1)
        if c>cmax: ncmax=max(ncmax,c-1)
    out=[[0]*w for _ in range(h)]
    for j in range(ncmin,ncmax+1):
        out[nrmin][j]=3; out[nrmax][j]=3
    for i in range(nrmin,nrmax+1):
        out[i][ncmin]=3; out[i][ncmax]=3
    for r,c in anchors:
        out[r][c]=6
    return out