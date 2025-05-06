def solve(grid):
    H=len(grid);W=len(grid[0])
    rmin=H; rmax=-1; cmin=W; cmax=-1
    for r in range(H):
        for c in range(W):
            if grid[r][c]!=0:
                if r<rmin:rmin=r
                if r>rmax:rmax=r
                if c<cmin:cmin=c
                if c>cmax:cmax=c
    h=rmax-rmin+1; w=cmax-cmin+1
    h2=(h+1)//2; w2=(w+1)//2
    return [row[cmin:cmin+w2] for row in grid[rmin:rmin+h2]]