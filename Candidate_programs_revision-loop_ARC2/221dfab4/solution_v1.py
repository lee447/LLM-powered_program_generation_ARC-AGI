def solve(grid):
    h, w = len(grid), len(grid[0])
    cols = set(c for row in grid for c in row if c not in (0,1))
    bar = max(cols, key=lambda c: any(grid[r][c0]==c and (r==0 or grid[r-1][c0]!=c) for r in range(h) for c0 in range(w)))
    inv = 3 if bar==4 else 4
    runs = []
    for r in range(h):
        c0=0
        while c0<w:
            if grid[r][c0]==bar:
                c1=c0
                while c1<w and grid[r][c1]==bar: c1+=1
                runs.append((r,c0,c1-c0))
                c0=c1
            else:
                c0+=1
    r0,c0,l0 = sorted(runs, key=lambda t:abs(t[0]-h//2))[0]
    bar_dir = 'S' if r0>h//2 else 'N' if r0<h//2 else 'E' if c0>w//2 else 'W'
    A = max(cols - {bar}, key=lambda c: sum(row.count(c) for row in grid))
    minr=minc=h; maxr=maxc=0
    for r in range(h):
        for c in range(w):
            if grid[r][c]==A:
                minr,minc=min(minr,r),min(minc,c)
                maxr,maxc=max(maxr,r),max(maxc,c)
    cr,cc=(minr+maxr)//2,(minc+maxc)//2
    def row_width(r):
        return sum(1 for c in range(w) if grid[r][c]==A)
    def col_height(c):
        return sum(1 for r in range(h) if grid[r][c]==A)
    # north
    rN = min(range(minr,maxr+1), key=lambda r: (r>cr, row_width(r)))+1
    # south
    rS = max(range(minr,maxr+1), key=lambda r: (r<cr, row_width(r)))-1
    # west
    cW = min(range(minc,maxc+1), key=lambda c: (c>cc, col_height(c)))+1
    # east
    cE = max(range(minc,maxc+1), key=lambda c: (c<cc, col_height(c)))-1
    out = [row[:] for row in grid]
    for d in ('N','E','S','W'):
        col = bar if d==bar_dir else inv
        if d=='N':
            r,c0n = rN, cc - l0//2
            for c in range(c0n, c0n+l0): out[r][c]=col
        elif d=='S':
            r,c0n = rS, cc - l0//2
            for c in range(c0n, c0n+l0): out[r][c]=col
        elif d=='W':
            c,r0n = cW, cr - l0//2
            for r in range(r0n, r0n+l0): out[r][c]=col
        else:  # E
            c,r0n = cE, cr - l0//2
            for r in range(r0n, r0n+l0): out[r][c]=col
    return out