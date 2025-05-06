def solve(grid):
    h=len(grid); w=len(grid[0])
    col=None
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                col=grid[i][j]; break
        if col is not None: break
    min_r=h; max_r=0; min_c=w; max_c=0
    for i in range(h):
        for j in range(w):
            if grid[i][j]==col:
                min_r=min(min_r,i); max_r=max(max_r,i)
                min_c=min(min_c,j); max_c=max(max_c,j)
    res=[row[:] for row in grid]
    for i in range(min_r+1,max_r):
        for j in range(min_c+1,max_c):
            res[i][j]=0
    d=max_r-min_r
    for t in range(d+1):
        r=min_r+t; c1=min_c+t; c2=max_c-t
        if 0<=r<h and 0<=c1<w: res[r][c1]=col
        if 0<=r<h and 0<=c2<w: res[r][c2]=col
    return res