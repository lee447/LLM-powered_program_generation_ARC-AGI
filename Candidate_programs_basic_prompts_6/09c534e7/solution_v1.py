def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    visited=[[False]*w for _ in range(h)]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                stack=[(i,j)]
                comp=[]
                visited[i][j]=True
                while stack:
                    r,c=stack.pop()
                    comp.append((r,c))
                    for dr,dc in dirs:
                        nr,nc=r+dr,c+dc
                        if 0<=nr<h and 0<=nc<w and not visited[nr][nc] and grid[nr][nc]==1:
                            visited[nr][nc]=True
                            stack.append((nr,nc))
                rs=[r for r,c in comp]; cs=[c for r,c in comp]
                r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
                if r1-r0>=2 and c1-c0>=2:
                    col=None
                    for r in range(r0+1,r1):
                        for c in range(c0+1,c1):
                            v=grid[r][c]
                            if v!=0 and v!=1:
                                col=v
                    if col is not None:
                        for r in range(r0+1,r1):
                            for c in range(c0+1,c1):
                                out[r][c]=col
    return out