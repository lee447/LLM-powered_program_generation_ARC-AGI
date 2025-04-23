def solve(grid):
    H=len(grid); W=len(grid[0])
    out=[row[:] for row in grid]
    for r in range(H):
        pts=[c for c in range(W) if grid[r][c]==6]
        if not pts: continue
        s,e=min(pts),max(pts)
        gs=[c for c in range(W) if grid[r][c]==3]
        L=max(c for c in gs if c<s); R=min(c for c in gs if c>e)
        left=grid[r][L+1:s]
        right=grid[r][e+1:R]
        w=R-L-1
        seg=[]
        for i in range(w):
            if i<len(left): seg.append(left[-1-i])
            else: seg.append(right[i-len(left)])
        for i,c in enumerate(range(L+1,R)):
            out[r][c]=seg[i]
        for c in pts:
            out[r][c]=0
    return out