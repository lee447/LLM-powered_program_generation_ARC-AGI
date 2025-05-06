def solve(grid):
    h=len(grid); w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]!=0 and not vis[r][c]:
                stack=[(r,c)]; vis[r][c]=True; cells=[]
                while stack:
                    rr,cc=stack.pop(); cells.append((rr,cc))
                    for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = rr+dr, cc+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not vis[nr][nc]:
                            vis[nr][nc]=True; stack.append((nr,nc))
                rs=[r for r,_ in cells]; cs=[c for _,c in cells]
                comps.append((min(rs),min(cs),max(rs),max(cs),cells))
    comps.sort(key=lambda x:(x[1],x[0]), reverse=True)
    out=[[0]*w for _ in range(h)]
    for min_r,min_c,max_r,max_c,cells in comps:
        max_shift=w-1-max_c
        for m in range(max_shift, -1, -1):
            ok=True
            for r,c in cells:
                if out[r][c+m]!=0:
                    ok=False; break
            if ok:
                for r,c in cells:
                    out[r][c+m]=grid[r][c]
                break
    return out