def solve(grid):
    rows,cols=len(grid),len(grid[0])
    rmin,cmin=rows,cols
    rmax,cmax=0,0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c]==5:
                rmin=min(rmin,r);rmax=max(rmax,r)
                cmin=min(cmin,c);cmax=max(cmax,c)
    region=[row[cmin:cmax+1] for row in grid[rmin:rmax+1]]
    res=[list(r) for r in region]
    H,W=len(res),len(res[0])
    border=res[0][0]
    cnt={}
    for i in range(H):
        for j in range(W):
            v=res[i][j]
            if v!=border:
                cnt[v]=cnt.get(v,0)+1
    bg=max(cnt,key=lambda k:cnt[k])
    shape_colors=[]
    for i in range(H):
        for j in range(W):
            v=res[i][j]
            if v!=border and v!=bg and v not in shape_colors:
                shape_colors.append(v)
    cands=sorted(set(range(10))-{border,bg}-set(shape_colors))
    if cands and cands[0]==0: cands=cands[1:]
    mapping={shape_colors[i]:cands[i] for i in range(len(shape_colors))}
    for i in range(H):
        for j in range(W):
            v=res[i][j]
            if v in mapping:
                res[i][j]=mapping[v]
    newc=set(mapping.values())
    for i in range(1,H-1):
        for j in range(1,W-1):
            v=res[i][j]
            if v in newc and res[i-1][j]==v and res[i+1][j]==v and res[i][j-1]==v and res[i][j+1]==v:
                res[i][j]=bg
    return res