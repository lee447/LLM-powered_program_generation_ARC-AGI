def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[row[:] for row in grid]
    hr=[]; hc=[]
    for r in range(h):
        cols=[c for c in range(w) if grid[r][c]==4]
        if len(cols)>=2: hr.append((r,sorted(cols)))
    for c in range(w):
        rows=[r for r in range(h) if grid[r][c]==4]
        if len(rows)>=2: hc.append((c,sorted(rows)))
    if hr:
        if len(hr)==1: m=(8,7)
        else: m=(6,0)
        for r,cols in hr:
            c1,c2=cols[0],cols[-1]
            iv=sorted({grid[r][c] for c in range(c1+1,c2)})
            mp={iv[i]:m[i] for i in range(len(iv))}
            for c in range(c1+1,c2): out[r][c]=mp[grid[r][c]]
    else:
        m=(8,7)
    for c,rows in hc:
        r1,r2=rows[0],rows[-1]
        iv=sorted({grid[r][c] for r in range(r1+1,r2)})
        mp={iv[i]:m[i] for i in range(len(iv))}
        for r in range(r1+1,r2): out[r][c]=mp[grid[r][c]]
    return out