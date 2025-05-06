def solve(grid):
    h,len_row= len(grid), len(grid[0])
    cnt={}
    for i in range(h):
        for j in range(len_row):
            cnt[grid[i][j]] = cnt.get(grid[i][j],0) + 1
    master = max((c for c in cnt if c!=0 and cnt[c]>1), key=lambda c:cnt[c])
    pts=[(i,j) for i in range(h) for j in range(len_row) if grid[i][j]==master]
    rmin=min(r for r,c in pts); rmax=max(r for r,c in pts)
    cmin=min(c for r,c in pts); cmax=max(c for r,c in pts)
    rowcnt={}
    for r,c in pts:
        lr=r-rmin
        rowcnt[lr]=rowcnt.get(lr,0)+1
    pivot_rows=[lr for lr,v in rowcnt.items() if v==1]
    anchors=[(c,[ (i,j) for i in range(h) for j in range(len_row) if grid[i][j]==c ][0]) for c in cnt if c!=0 and c!=master and cnt[c]==1]
    res=[row[:] for row in grid]
    for color, (ra,ca) in anchors:
        lra=ra-rmin
        pr=min(pivot_rows, key=lambda lr:abs(lr-lra))
        prg=rmin+pr
        pcg=next(c for r,c in pts if r==prg)
        for r,c in pts:
            dr,dc=r-prg,c-pcg
            if ca<cmin or ca>cmax:
                dr2,dc2=dr,-dc
            else:
                dr2,dc2=-dr,dc
            rr,cc=ra+dr2,ca+dc2
            if 0<=rr<h and 0<=cc<len_row and res[rr][cc]==0:
                res[rr][cc]=color
    return res