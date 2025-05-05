def solve(grid):
    h=len(grid)
    w=len(grid[0])
    rmin=h
    rmax=-1
    cmin=w
    cmax=-1
    for i in range(h):
        for j in range(w):
            if grid[i][j]!=0:
                if i<rmin: rmin=i
                if i>rmax: rmax=i
                if j<cmin: cmin=j
                if j>cmax: cmax=j
    for r in range(rmin+1,rmax):
        if all(grid[r][j]==0 for j in range(w)):
            for j in range(w):
                grid[r][j]=3
            return grid
    for c in range(cmin+1,cmax):
        if all(grid[i][c]==0 for i in range(h)):
            for i in range(h):
                grid[i][c]=3
            return grid
    return grid