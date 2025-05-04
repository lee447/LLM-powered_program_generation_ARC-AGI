def solve(grid):
    h=len(grid)
    w=len(grid[0]) if h else 0
    bounds={}
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v:
                if v in bounds:
                    mn,mx=bounds[v]
                    bounds[v]=(min(mn,r),max(mx,r))
                else:
                    bounds[v]=(r,r)
    res=[[0]*w for _ in range(h)]
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v:
                mn,mx=bounds[v]
                nr=mn+mx-r
                res[nr][c]=v
    return res