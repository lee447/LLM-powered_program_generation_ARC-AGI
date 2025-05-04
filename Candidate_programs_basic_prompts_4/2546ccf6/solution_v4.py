def solve(grid):
    H=len(grid); W=len(grid[0])
    freq={}
    for r in range(H):
        for c in range(W):
            freq[grid[r][c]]=freq.get(grid[r][c],0)+1
    bg=max(freq,key=lambda k:freq[k])
    barrier=None
    for k,v in sorted(freq.items(), key=lambda x:-x[1]):
        if k!=bg:
            barrier=k
            break
    bar_rows=[i for i in range(H) if all(grid[i][j]==barrier for j in range(W))]
    bar_cols=[j for j in range(W) if all(grid[i][j]==barrier for i in range(H))]
    bar_rows.sort(); bar_cols.sort()
    row_segs=[]; prev=-1
    for br in bar_rows:
        if br-prev>1: row_segs.append((prev+1,br-1))
        prev=br
    if prev< H-1: row_segs.append((prev+1,H-1))
    col_segs=[]; prev=-1
    for bc in bar_cols:
        if bc-prev>1: col_segs.append((prev+1,bc-1))
        prev=bc
    if prev< W-1: col_segs.append((prev+1,W-1))
    cell_shapes={}
    for i,(r0,r1) in enumerate(row_segs):
        for j,(c0,c1) in enumerate(col_segs):
            pts=[]
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    v=grid[r][c]
                    if v!=bg and v!=barrier: pts.append((r,c,v))
            cell_shapes[(i,j)]=pts
    for (i,j),pts in list(cell_shapes.items()):
        if pts: continue
        neighbor=None; d=None
        if (i,j-1) in cell_shapes and cell_shapes[(i,j-1)]:
            neighbor=(i,j-1); d='h'
        elif (i,j+1) in cell_shapes and cell_shapes[(i,j+1)]:
            neighbor=(i,j+1); d='h'
        elif (i-1,j) in cell_shapes and cell_shapes[(i-1,j)]:
            neighbor=(i-1,j); d='v'
        elif (i+1,j) in cell_shapes and cell_shapes[(i+1,j)]:
            neighbor=(i+1,j); d='v'
        if not neighbor: continue
        ni,nj=neighbor
        if d=='h':
            bcol=bar_cols[min(nj,j)]
        else:
            brow=bar_rows[min(ni,i)]
        for (r,c,v) in cell_shapes[(ni,nj)]:
            if d=='h':
                nc=bcol-(c-bcol); nr=r
            else:
                nr=brow-(r-brow); nc=c
            grid[nr][nc]=v
    return grid