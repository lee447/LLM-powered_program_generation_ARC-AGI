def solve(grid):
    h=len(grid);w=len(grid[0])
    out=[row[:] for row in grid]
    vis=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==3 and not vis[i][j]:
                stack=[(i,j)];comp=[]
                vis[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and grid[nr][nc]==3:
                            vis[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,_ in comp]; cs=[c for _,c in comp]
                r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
                if r1-r0>=2 and maxc-minc>=2:
                    border=set()
                    for c in range(minc,maxc+1):
                        border.add((r0,c));border.add((r1,c))
                    for r in range(r0,r1+1):
                        border.add((r,minc));border.add((r,maxc))
                    if len(comp)==len(border):
                        for r in range(r0+1,r1):
                            for c in range(minc+1,maxc):
                                if out[r][c]==0:
                                    out[r][c]=3
    return out