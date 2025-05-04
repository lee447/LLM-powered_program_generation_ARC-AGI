def solve(grid):
    h=len(grid); w=len(grid[0])
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0 and not visited[i][j]:
                c=grid[i][j]
                stack=[(i,j)]
                visited[i][j]=True
                pts=[]
                while stack:
                    x,y=stack.pop()
                    pts.append((x,y))
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and not visited[nx][ny] and grid[nx][ny]==c:
                            visited[nx][ny]=True
                            stack.append((nx,ny))
                comps.append((c,pts))
    def has_hole(pts):
        rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
        r0,r1=min(rs),max(rs); c0,c1=min(cs),max(cs)
        inside=set((r,c) for r in range(r0,r1+1) for c in range(c0,c1+1) if grid[r][c]==0)
        seen=set()
        for p in list(inside):
            if p not in seen:
                stack=[p]; region=[p]; seen.add(p)
                touches=False
                while stack:
                    x,y=stack.pop()
                    if x==r0 or x==r1 or y==c0 or y==c1: touches=True
                    for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                        nx,ny=x+dx,y+dy
                        if (nx,ny) in inside and (nx,ny) not in seen:
                            seen.add((nx,ny)); stack.append((nx,ny)); region.append((nx,ny))
                if not touches:
                    return True
        return False
    target=None
    for c,pts in comps:
        if has_hole(pts):
            target=(c,pts); break
    if target is None:
        target=comps[0]
    c,pts=target
    rs=[p[0] for p in pts]; cs=[p[1] for p in pts]
    r0,r1,minc,maxc=min(rs),max(rs),min(cs),max(cs)
    out=[[0]*(maxc-minc+1) for _ in range(r1-r0+1)]
    for x,y in pts:
        out[x-r0][y-minc]=c
    return out