def solve(grid):
    h=len(grid);w=len(grid[0])
    legend_cells=[(r,c) for r in range(h) for c in range(w) if grid[r][c]>1]
    if not legend_cells:
        return grid
    lr0=min(r for r,c in legend_cells); lr1=max(r for r,c in legend_cells)
    lc0=min(c for r,c in legend_cells); lc1=max(c for r,c in legend_cells)
    legend=[row[lc0:lc1+1] for row in grid[lr0:lr1+1]]
    lh=len(legend); lw=len(legend[0])
    visited=[[False]*w for _ in range(h)]
    comps=[]
    for r in range(h):
        for c in range(w):
            if grid[r][c]==1 and not visited[r][c]:
                stack=[(r,c)];visited[r][c]=True;pts=[]
                while stack:
                    y,x=stack.pop()
                    pts.append((y,x))
                    for dy,dx in ((1,0),(-1,0),(0,1),(0,-1)):
                        ny,nx=y+dy,x+dx
                        if 0<=ny<h and 0<=nx<w and grid[ny][nx]==1 and not visited[ny][nx]:
                            visited[ny][nx]=True;stack.append((ny,nx))
                mr=min(y for y,x in pts); mc=min(x for y,x in pts)
                comps.append((mr,mc,pts))
    row_idxs=sorted(set(mr for mr,mc,pts in comps))
    col_idxs=sorted(set(mc for mr,mc,pts in comps))
    out=[row[:] for row in grid]
    for mr,mc,pts in comps:
        i=row_idxs.index(mr); j=col_idxs.index(mc)
        color=legend[i][j]
        for y,x in pts:
            out[y][x]=color
    return out