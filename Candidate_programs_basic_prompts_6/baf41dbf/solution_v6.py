def solve(grid):
    R=len(grid); C=len(grid[0])
    S=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==3]
    if not S: return [row[:] for row in grid]
    minr=min(r for r,c in S); maxr=max(r for r,c in S)
    minc=min(c for r,c in S); maxc=max(c for r,c in S)
    M=[(r,c) for r in range(R) for c in range(C) if grid[r][c]==6]
    lc=[c for r,c in M if minr<=r<=maxr and c<minc]
    rc=[c for r,c in M if minr<=r<=maxr and c>maxc]
    tc=[r for r,c in M if minc<=c<=maxc and r<minr]
    bc=[r for r,c in M if minc<=c<=maxc and r>maxr]
    left=(max(lc)+1) if lc else minc
    right=(min(rc)-1) if rc else maxc
    top=(max(tc)+1) if tc else minr
    bottom=(min(bc)-1) if bc else maxr
    res=[row[:] for row in grid]
    for r,c in S: res[r][c]=0
    for c in range(left,right+1):
        if res[top][c]!=6: res[top][c]=3
        if res[bottom][c]!=6: res[bottom][c]=3
    for r in range(top,bottom+1):
        if res[r][left]!=6: res[r][left]=3
        if res[r][right]!=6: res[r][right]=3
    return res