def solve(grid):
    h=len(grid); w=len(grid[0])
    centers=[]
    for r in range(1,h-1):
        for c in range(1,w-1):
            if grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3 and grid[r][c-1]==3 and grid[r][c+1]==3:
                centers.append((r,c))
    out=[row[:] for row in grid]
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr=r2-r1; dc=c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                step_r=dr//abs(dr); step_c=dc//abs(dc)
                rr,cc=r1+step_r,c1+step_c
                while (rr,cc)!=(r2,c2):
                    out[rr][cc]=2
                    rr+=step_r; cc+=step_c
    return out