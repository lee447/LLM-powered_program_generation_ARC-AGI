def solve(grid):
    h=len(grid); w=len(grid[0])
    pts=[(i,j) for i in range(h) for j in range(w) if grid[i][j]==8]
    s=set(pts)
    degs={p:sum(((p[0]+d[0],p[1]+d[1]) in s) for d in [(1,0),(-1,0),(0,1),(0,-1)]) for p in pts}
    p0=max(degs, key=lambda p:degs[p])
    M=[(i-p0[0], j-p0[1]) for i,j in pts]
    def rot_once(ms):
        return [(-dc, dr) for dr,dc in ms]
    R=[M]
    for _ in range(3):
        R.append(rot_once(R[-1]))
    new=set()
    for Mr in R:
        drs=[d[0] for d in Mr]; dcs=[d[1] for d in Mr]
        rmin, rmax, cmin, cmax = min(drs), max(drs), min(dcs), max(dcs)
        for i in range(-rmin, h-rmax):
            for j in range(-cmin, w-cmax):
                C=None; ok=True
                for dr,dc in Mr:
                    v=grid[i+dr][j+dc]
                    if v==8:
                        ok=False; break
                    if C is None:
                        C=v
                    elif v!=C:
                        ok=False; break
                if ok and C is not None:
                    for dr,dc in Mr:
                        new.add((i+dr, j+dc))
    res=[row[:] for row in grid]
    for i,j in new:
        res[i][j]=8
    return res