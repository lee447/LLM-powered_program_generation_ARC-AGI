def solve(grid):
    n=len(grid); m=len(grid[0])
    out=[[0]*m for _ in range(n)]
    last=n-1
    for c in range(m):
        if grid[last][c]!=0:
            pts=[(r,grid[r][c]) for r in range(n) if grid[r][c]!=0]
            pts.sort()
            prev=-1
            for r,v in pts:
                for i in range(prev+1,r+1):
                    out[i][c]=v
                prev=r
        else:
            for r in range(n):
                if grid[r][c]!=0:
                    out[r][c]=grid[r][c]
    return out