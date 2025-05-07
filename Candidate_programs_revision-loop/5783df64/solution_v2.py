def solve(grid):
    n=len(grid)
    m=len(grid[0])
    h=n//3
    w=m//3
    res=[[0]*3 for _ in range(3)]
    for bi in range(3):
        for bj in range(3):
            for i in range(bi*h,(bi+1)*h):
                for j in range(bj*w,(bj+1)*w):
                    if grid[i][j]!=0:
                        res[bi][bj]=grid[i][j]
    return res