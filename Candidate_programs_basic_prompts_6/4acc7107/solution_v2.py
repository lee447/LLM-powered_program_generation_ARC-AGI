def solve(grid):
    h=len(grid); w=len(grid[0])
    cells={}
    for r in range(h):
        for c in range(w):
            v=grid[r][c]
            if v:
                cells.setdefault(v,[]).append((r,c))
    res=[[0]*w for _ in range(h)]
    for v,pts in cells.items():
        minr=min(r for r,c in pts)
        minc=min(c for r,c in pts)
        maxr=max(r for r,c in pts)
        maxc=max(c for r,c in pts)
        ph=maxr-minr+1; pw=maxc-minc+1
        if v==sorted(cells)[0]:
            dr=h-ph; dc=0
        else:
            dr=h-ph; dc=w-pw
        for r,c in pts:
            res[r-minr+dr][c-minc+dc]=v
    return res