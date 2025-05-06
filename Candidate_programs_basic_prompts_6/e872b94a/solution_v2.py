def solve(grid):
    h=len(grid); w=len(grid[0])
    count5=[sum(1 for r in range(h) if grid[r][c]==5) for c in range(w)]
    blank_cols=[c for c in range(w) if count5[c]==0]
    if blank_cols:
        inter=[c for c in blank_cols if 0<c<w-1]
        c=inter[0] if inter else blank_cols[0]
        if c>0 and count5[c-1]>0:
            nbr=c-1
        else:
            nbr=c+1
    else:
        m=min(count5)
        cands=[c for c in range(w) if count5[c]==m]
        bdy=[c for c in cands if c==0 or c==w-1]
        c=bdy[0] if bdy else cands[0]
        if c>0 and (c==w-1 or count5[c-1]>=count5[c+1]):
            nbr=c-1
        else:
            nbr=c+1
    res=[]
    for r in range(h):
        if 0<=nbr<w and grid[r][nbr]==5:
            res.append([0])
    return res