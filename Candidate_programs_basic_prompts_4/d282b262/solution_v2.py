def solve(grid):
    h=len(grid);w=len(grid[0])
    vis=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not vis[i][j]:
                stack=[(i,j)];vis[i][j]=True;cells=[]
                while stack:
                    r,c=stack.pop()
                    cells.append((r,c))
                    for dr,dc in((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0<=nr<h and 0<=nc<w and grid[nr][nc]!=0 and not vis[nr][nc]:
                            vis[nr][nc]=True;stack.append((nr,nc))
                comps.append(cells)
    occ=[[None]*w for _ in range(h)]
    for idx,c in enumerate(comps):
        for r,c0 in c: occ[r][c0]=idx
    moved=True
    while moved:
        moved=False
        can_move=[True]*len(comps)
        for idx,c in enumerate(comps):
            for r,c0 in c:
                nc=c0+1
                if nc>=w or (occ[r][nc] is not None and occ[r][nc]!=idx):
                    can_move[idx]=False;break
        for idx in range(len(comps)):
            if can_move[idx]:
                moved=True
                for r,c0 in comps[idx]:
                    occ[r][c0]=None
                for k in range(len(comps[idx])):
                    r,c0=comps[idx][k];comps[idx][k]=(r,c0+1)
                for r,c0 in comps[idx]:
                    occ[r][c0]=idx
    out=[[0]*w for _ in range(h)]
    for idx,c in enumerate(comps):
        for r,c0 in c:
            out[r][c0]=grid[r][c0]
    return out