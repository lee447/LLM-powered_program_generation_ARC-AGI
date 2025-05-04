def solve(grid):
    rmin=len(grid); rmax=-1; cmin=len(grid[0]); cmax=-1
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j]!=0:
                if i<rmin: rmin=i
                if i>rmax: rmax=i
                if j<cmin: cmin=j
                if j>cmax: cmax=j
    h=rmax-rmin+1; w=cmax-cmin+1
    hr=(h+1)//2; wr=(w+1)//2
    return [grid[rmin+i][cmin:cmin+wr] for i in range(hr)]