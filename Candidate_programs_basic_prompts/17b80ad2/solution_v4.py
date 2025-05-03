def solve(grid):
    h=len(grid);w=len(grid[0])
    res=[row[:] for row in grid]
    last=h-1
    seg=[c for c in range(w) if grid[last][c]!=0]
    for c in seg:
        pts=[(r,grid[r][c]) for r in range(h) if grid[r][c]!=0]
        pts.sort()
        rows=[r for r,v in pts];vals=[v for r,v in pts]
        for i,(r0,v) in enumerate(zip(rows,vals)):
            start=rows[i-1]+1 if i>0 else 0
            for r in range(start,r0+1):
                res[r][c]=v
    return res