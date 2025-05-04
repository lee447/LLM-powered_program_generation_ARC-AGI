def solve(grid):
    h=len(grid); w=len(grid[0])
    orig=[row[:] for row in grid]
    out=[row[:] for row in grid]
    dirs=[(-1,0),(1,0),(0,-1),(0,1)]
    for r in range(h):
        for c in range(w):
            if orig[r][c]>1:
                seed_val=orig[r][c]
                vis={(r,c)}
                stack=[(r,c)]
                while stack:
                    x,y=stack.pop()
                    for dx,dy in dirs:
                        nx,ny=x+dx,y+dy
                        if 0<=nx<h and 0<=ny<w and (nx,ny) not in vis and orig[nx][ny]>0:
                            vis.add((nx,ny)); stack.append((nx,ny))
                for x,y in vis:
                    if orig[x][y]==1:
                        ok=True
                        for dx,dy in dirs:
                            nx,ny=x+dx,y+dy
                            if not(0<=nx<h and 0<=ny<w and orig[nx][ny]>0):
                                ok=False; break
                        if ok:
                            out[x][y]=seed_val
    return out