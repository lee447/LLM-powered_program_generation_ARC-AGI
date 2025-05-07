def solve(grid):
    h=len(grid); w=len(grid[0])
    g=[row[:] for row in grid]
    ref_vis=[[False]*w for _ in range(h)]
    dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    ref_cells=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]>1 and not ref_vis[i][j]:
                q=[(i,j)]; ref_vis[i][j]=True
                while q:
                    r,c=q.pop()
                    ref_cells.append((r,c))
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]>1 and not ref_vis[nr][nc]:
                            ref_vis[nr][nc]=True
                            q.append((nr,nc))
                break
        if ref_cells: break
    rs=[r for r,c in ref_cells]; cs=[c for r,c in ref_cells]
    r0, c0 = min(rs), min(cs)
    mask = {(r-r0,c-c0): grid[r][c] for r,c in ref_cells}
    vis=[[False]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not vis[i][j]:
                q=[(i,j)]; comp=[(i,j)]; vis[i][j]=True
                while q:
                    r,c=q.pop()
                    for dr,dc in dirs:
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]==1 and not vis[nr][nc]:
                            vis[nr][nc]=True
                            q.append((nr,nc)); comp.append((nr,nc))
                rs2=[r for r,c in comp]; cs2=[c for r,c in comp]
                r1, c1 = min(rs2), min(cs2)
                offs = {(r-r1,c-c1) for r,c in comp}
                if offs==set(mask.keys()):
                    for (dr,dc),col in mask.items():
                        g[r1+dr][c1+dc]=col
    return g