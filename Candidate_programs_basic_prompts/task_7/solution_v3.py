def solve(grid):
    R, C = len(grid), len(grid[0])
    marks = [(r, len(set(grid[r]))==1 and grid[r][0] or None) for r in range(R)]
    hr = [r for r in range(R) if all(grid[r][c]==grid[r][0] for c in range(C))]
    hc = [c for c in range(C) if all(grid[r][c]==grid[0][c] for r in range(R))]
    dr = sorted(hr)
    dc = sorted(hc)
    subrs = []
    prev = -1
    for r in dr+[R]:
        if r-prev>1:
            subrs.append((prev+1, r-1))
        prev = r
    subcs = []
    prev = -1
    for c in dc+[C]:
        if c-prev>1:
            subcs.append((prev+1, c-1))
        prev = c
    Cval = max(v for row in grid for v in row if v not in (0,1,4))
    out = [row[:] for row in grid]
    for r0,r1 in subrs:
        for c0,c1 in subcs:
            ones = [(r,c) for r in range(r0,r1+1) for c in range(c0,c1+1) if grid[r][c]==1]
            if not ones: continue
            top = min(r for r,_ in ones)
            midc = (c0+c1)//2
            for r,c in ones:
                if r==top and (c==c0 or c==c1): out[r][c]=Cval
                elif r==top+1 and c==midc: out[r][c]=Cval
    return out