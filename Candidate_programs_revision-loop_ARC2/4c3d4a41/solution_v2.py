def solve(grid):
    h,len_row=len(grid),len(grid[0])
    top=[i for i in range(len_row) if grid[0][i]==5][0]
    left=[r for r in range(h) if grid[r][top]==5][0]
    bottom=[i for i in range(len_row) if grid[h-1][i]==5][0]
    right=[r for r in range(h) if grid[r][bottom]==5][0]
    r0,c0,r1,c1=left,top,right,bottom
    mid=(c0+c1)//2
    out=[row[:] for row in grid]
    for r in range(r0+1,r1):
        rr=r-r0
        for c in range(c0+1,c1):
            dl=c-c0; dr=c1-c
            if rr>min(dl,dr):
                out[r][c]=5
    return out