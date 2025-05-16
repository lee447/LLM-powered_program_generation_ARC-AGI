def solve(grid):
    rows=len(grid)
    cols=len(grid[0])
    rmin=rows; rmax=0; cmin=cols; cmax=0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==5:
                if r<rmin: rmin=r
                if r>rmax: rmax=r
                if c<cmin: cmin=c
                if c>cmax: cmax=c
    return [row[cmin:cmax+1] for row in grid[rmin:rmax+1]]