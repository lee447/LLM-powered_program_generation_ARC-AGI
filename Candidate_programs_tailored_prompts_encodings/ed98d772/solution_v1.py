def solve(grid):
    h=len(grid)
    w=len(grid[0])
    H=2*h
    W=2*w
    out=[[0]*W for _ in range(H)]
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v!=0:
                out[i][j]=v
                out[i][W-1-j]=v
                out[H-1-i][j]=v
                out[H-1-i][W-1-j]=v
    return out