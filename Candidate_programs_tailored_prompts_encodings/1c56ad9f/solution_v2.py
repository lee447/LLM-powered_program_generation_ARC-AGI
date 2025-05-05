def solve(grid):
    h, w = len(grid), len(grid[0])
    res = [[0]*w for _ in range(h)]
    pts = [(r,c,grid[r][c]) for r in range(h) for c in range(w) if grid[r][c]]
    if not pts: return res
    color = pts[0][2]
    rows = sorted({r for r,c,v in pts if any(grid[r][cc]==color for cc in range(w)) and sum(grid[r][cc]==color for cc in range(w))>2})
    def hshift(r, c):
        i = rows.index(r)
        return c + (1 if i%2==1 else 0)
    def vshift(r, c):
        i = max(i for i,rr in enumerate(rows) if rr<r)
        d = r-rows[i]
        seg = d-1
        if seg<0: return c
        m = seg%4
        if m==0: return c-1
        if m==2: return c+1
        return c
    for r,c,v in pts:
        if r in rows:
            nc = hshift(r,c)
        else:
            nc = vshift(r,c)
        res[r][nc] = v
    return res