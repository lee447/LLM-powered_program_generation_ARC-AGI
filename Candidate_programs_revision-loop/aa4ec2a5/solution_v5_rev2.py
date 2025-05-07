import collections
def solve(grid):
    h,w=len(grid),len(grid[0])
    dirs=[(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==1 and not visited[i][j]:
                q=[(i,j)]
                visited[i][j]=True
                pts=[(i,j)]
                for x,y in q:
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and grid[nx][ny]==1 and not visited[nx][ny]:
                            visited[nx][ny]=True
                            q.append((nx,ny))
                            pts.append((nx,ny))
                comps.append(pts)
    if not comps:
        return grid
    sizes=[len(c) for c in comps]
    largest_index=sizes.index(max(sizes))
    out=[row[:] for row in grid]
    orig=grid
    for idx,comp in enumerate(comps):
        layers=3 if idx==largest_index else 1
        prev=set(comp)
        used=set(comp)
        for k in range(1,layers+1):
            nxt=set()
            for x,y in prev:
                for dx,dy in dirs:
                    nx,ny=x+dx,y+dy
                    if 0<=nx<h and 0<=ny<w and orig[nx][ny]==4 and (nx,ny) not in used:
                        nxt.add((nx,ny))
            color=2 if k==1 else (8 if k==2 else 6)
            for x,y in nxt:
                out[x][y]=color
            used |= nxt
            prev=nxt
    return out