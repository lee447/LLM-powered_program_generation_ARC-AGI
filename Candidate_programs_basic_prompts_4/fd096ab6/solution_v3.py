def solve(grid):
    h=len(grid)
    w=len(grid[0])
    res=[row[:] for row in grid]
    regions={}
    for i in range(h):
        for j in range(w):
            c=grid[i][j]
            if c not in (0,1,4):
                if c not in regions: regions[c]=[i,i,j,j]
                else:
                    regions[c][0]=min(regions[c][0],i)
                    regions[c][1]=max(regions[c][1],i)
                    regions[c][2]=min(regions[c][2],j)
                    regions[c][3]=max(regions[c][3],j)
    for c,(r0,r1,c0,c1) in regions.items():
        for i in range(r0,r1+1):
            for j in range(c0,c1+1):
                res[i][j]=c
    return res