def solve(grid):
    R=len(grid)
    C=len(grid[0]) if R>0 else 0
    centers=[]
    for r in range(1,R-1):
        for c in range(1,C-1):
            if (grid[r][c]==3 and grid[r-1][c]==3 and grid[r+1][c]==3
                and grid[r][c-1]==3 and grid[r][c+1]==3):
                centers.append((r,c))
    output=[row[:] for row in grid]
    for i in range(len(centers)):
        r1,c1=centers[i]
        for j in range(i+1,len(centers)):
            r2,c2=centers[j]
            dr=r2-r1
            dc=c2-c1
            if abs(dr)==abs(dc) and dr!=0:
                step_r=(dr>0)-(dr<0)
                step_c=(dc>0)-(dc<0)
                for k in range(1,abs(dr)):
                    rr=r1+step_r*k
                    cc=c1+step_c*k
                    if output[rr][cc]==0:
                        output[rr][cc]=2
    return output