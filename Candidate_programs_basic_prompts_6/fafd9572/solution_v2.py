def solve(grid):
    H=len(grid);W=len(grid[0]) if H else 0
    seed_rows=sorted({r for r in range(H) for c in range(W) if grid[r][c]>1})
    seed_cols=sorted({c for r in range(H) for c in range(W) if grid[r][c]>1})
    comp_id=[[-1]*W for _ in range(H)]
    comps=[];bounds=[]
    dirs=[(1,0),(-1,0),(0,1),(0,-1)]
    cid=0
    for r in range(H):
        for c in range(W):
            if grid[r][c]==1 and comp_id[r][c]==-1:
                stack=[(r,c)];comp_id[r][c]=cid
                pts=[];mr,mc=r,c
                while stack:
                    x,y=stack.pop();pts.append((x,y))
                    if x<mr:mr=x
                    if y<mc:mc=y
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<H and 0<=ny<W and grid[nx][ny]==1 and comp_id[nx][ny]==-1:
                            comp_id[nx][ny]=cid;stack.append((nx,ny))
                comps.append(pts);bounds.append((mr,mc));cid+=1
    row_vals=sorted({r for r,_ in bounds});col_vals=sorted({c for _,c in bounds})
    row_to_i={v:i for i,v in enumerate(row_vals)}
    col_to_j={v:j for j,v in enumerate(col_vals)}
    out=[row[:] for row in grid]
    for k,(mr,mc) in enumerate(bounds):
        i=row_to_i[mr];j=col_to_j[mc]
        col=grid[seed_rows[i]][seed_cols[j]]
        for x,y in comps[k]:
            out[x][y]=col
    return out