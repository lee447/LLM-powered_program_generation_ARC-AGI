def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[[0]*w for _ in range(h)]
    colors=set()
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0: colors.add(grid[i][j])
    for c in colors:
        imin=h; imax=-1; jmin=w; jmax=-1
        for i in range(h):
            for j in range(w):
                if grid[i][j]==c:
                    if i<imin: imin=i
                    if i>imax: imax=i
                    if j<jmin: jmin=j
                    if j>jmax: jmax=j
        hsub=imax-imin+1; wsub=jmax-jmin+1
        for di in range(hsub):
            for dj in range(wsub):
                if grid[imax-di][jmax-dj]==c:
                    out[imin+di][jmin+dj]=c
    return out