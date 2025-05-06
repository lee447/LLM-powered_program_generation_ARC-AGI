def solve(grid):
    h=len(grid);w=len(grid[0])
    threes=[(r,c)for r in range(h)for c in range(w)if grid[r][c]==3]
    minsr=min(r for r,c in threes);maxsr=max(r for r,c in threes)
    minsc=min(c for r,c in threes);maxsc=max(c for r,c in threes)
    minr, maxr, minc, maxc = minsr, maxsr, minsc, maxsc
    for r in range(h):
        for c in range(w):
            if grid[r][c]==6:
                if c<minc: minc=c+1
                if c>maxc: maxc=c-1
                if r<minr: minr=r+1
                if r>maxr: maxr=r-1
    out=[row[:] for row in grid]
    for r in range(minr, maxr+1):
        for c in range(minc, maxc+1):
            if (r==minr or r==maxr or c==minc or c==maxc) and out[r][c]!=6:
                out[r][c]=3
    return out