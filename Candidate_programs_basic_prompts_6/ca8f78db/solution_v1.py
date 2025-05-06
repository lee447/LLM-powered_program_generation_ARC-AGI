def solve(grid):
    H=len(grid); W=len(grid[0])
    def find_period(dim, get):
        for p in range(1, dim):
            ok=True
            for i in range(dim-p):
                for j in range(W if get is None else dim):
                    a=get(i,j) if get else grid[i][j]
                    b=get(i+p,j) if get else grid[i+p][j]
                    if a and b and a!=b:
                        ok=False; break
                if not ok: break
            if ok: return p
        return dim
    th=find_period(H, None)
    tw=find_period(W, None)
    tile=[[None]*tw for _ in range(th)]
    for i in range(H):
        for j in range(W):
            v=grid[i][j]
            if v:
                ti, tj=i%th, j%tw
                if tile[ti][tj] is None:
                    tile[ti][tj]=v
    res=[row[:] for row in grid]
    for i in range(H):
        for j in range(W):
            if res[i][j]==0:
                res[i][j]=tile[i%th][j%tw]
    return res