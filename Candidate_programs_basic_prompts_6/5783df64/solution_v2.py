def solve(grid):
    H=len(grid)
    W=len(grid[0])
    bh=H//3
    bw=W//3
    res=[[0]*3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            s=0
            for r in range(i*bh,(i+1)*bh):
                for c in range(j*bw,(j+1)*bw):
                    s+=grid[r][c]
            res[i][j]=s
    return res