def solve(grid):
    h=len(grid); w=len(grid[0])
    res=[row[:] for row in grid]
    vis=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not vis[i][j]:
                stack=[(i,j)]; comp=[]; marker=None
                while stack:
                    r,c=stack.pop()
                    if vis[r][c]: continue
                    vis[r][c]=True
                    comp.append((r,c))
                    if grid[r][c]!=1:
                        marker=grid[r][c]
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not vis[nr][nc]:
                            stack.append((nr,nc))
                if marker is not None:
                    rs=[r for r,c in comp]; cs=[c for r,c in comp]
                    rmin,rmax=min(rs),max(rs); cmin,cmax=min(cs),max(cs)
                    for rr in range(rmin+1,rmax):
                        for cc in range(cmin+1,cmax):
                            res[rr][cc]=marker
    return res