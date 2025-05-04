def solve(grid):
    h=len(grid)
    w=len(grid[0]) if h else 0
    min_r={}
    max_r={}
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v:
                if v in min_r:
                    if i<min_r[v]: min_r[v]=i
                    if i>max_r[v]: max_r[v]=i
                else:
                    min_r[v]=i
                    max_r[v]=i
    out=[[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            v=grid[i][j]
            if v:
                i2=min_r[v]+max_r[v]-i
                out[i2][j]=v
    return out