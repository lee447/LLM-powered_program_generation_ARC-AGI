def solve(grid):
    R=len(grid); C=len(grid[0])
    col=None
    for i in range(R):
        for j in range(C):
            if grid[i][j]!=0:
                col=grid[i][j]; break
        if col is not None: break
    visited=[[False]*C for _ in range(R)]
    comps=[]
    for i in range(R):
        for j in range(C):
            if grid[i][j]==col and not visited[i][j]:
                stack=[(i,j)]
                visited[i][j]=True
                comp=[]
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<R and 0<=nc<C and not visited[nr][nc] and grid[nr][nc]==col:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                comps.append(comp)
    comps=sorted(comps, key=len, reverse=True)[:3]
    coords_local=[]
    dims=[]
    for comp in comps:
        rs=[r for r,c in comp]; cs=[c for r,c in comp]
        minr, maxr = min(rs), max(rs)
        minc, maxc = min(cs), max(cs)
        H=maxr-minr+1; W=maxc-minc+1
        dims.append((H,W))
        s=set()
        for r,c in comp:
            s.add((r-minr, c-minc))
        coords_local.append(s)
    def rotate(coords, H, W, t):
        if t==0: return coords, H, W
        if t==1:
            nc=set()
            for r,c in coords: nc.add((c, H-1-r))
            return nc, W, H
        if t==2:
            nc=set()
            for r,c in coords: nc.add((H-1-r, W-1-c))
            return nc, H, W
        nc=set()
        for r,c in coords: nc.add((W-1-c, r))
        return nc, W, H
    base=coords_local[0]
    aligned=[base]
    for k in (1,2):
        best_set=None; best_count=-1
        Hk,Wk=dims[k]
        for t in range(4):
            rotk, Hr, Wr = rotate(coords_local[k], Hk, Wk, t)
            dc={}
            for r1,c1 in base:
                for r2,c2 in rotk:
                    d=(r1-r2, c1-c2)
                    dc[d]=dc.get(d,0)+1
            dr,dc0=max(dc.items(), key=lambda x:x[1])[0]
            if dc[(dr,dc0)]>best_count:
                best_count=dc[(dr,dc0)]
                best_set=set((r2+dr, c2+dc0) for r2,c2 in rotk)
        aligned.append(best_set)
    common = aligned[0] & aligned[1] & aligned[2]
    rs=[r for r,c in common]; cs=[c for r,c in common]
    minr,minc=min(rs),min(cs); maxr,maxc=max(rs),max(cs)
    Hout=maxr-minr+1; Wout=maxc-minc+1
    out=[[0]*Wout for _ in range(Hout)]
    for r,c in common:
        out[r-minr][c-minc]=col
    return out