def solve(grid):
    h=len(grid); w=len(grid[0])
    row_seps=[i for i in range(h) if all(grid[i][j]==0 for j in range(w))]
    col_seps=[j for j in range(w) if all(grid[i][j]==0 for i in range(h))]
    row_ranges=[]
    prev=-1
    for r in row_seps:
        if r-prev>1: row_ranges.append(list(range(prev+1,r)))
        prev=r
    prev=-1
    col_ranges=[]
    for c in col_seps:
        if c-prev>1: col_ranges.append(list(range(prev+1,c)))
        prev=c
    R=len(row_ranges); C=len(col_ranges)
    data=[[None]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            rows=row_ranges[i]; cols=col_ranges[j]
            cnt={}
            for r in rows:
                for c in cols:
                    v=grid[r][c]
                    if v!=0: cnt[v]=cnt.get(v,0)+1
            cs=list(cnt.items())
            c1,c2=cs[0][0],cs[1][0]
            if cnt[c1]<cnt[c2]: ac, bg=c1,c2
            else: ac, bg=c2,c1
            shape=[]
            for idx_r,r in enumerate(rows):
                for idx_c,c in enumerate(cols):
                    if grid[r][c]==ac: shape.append((idx_r,idx_c))
            data[i][j]=(bg,ac,shape)
    out=[row[:] for row in grid]
    for i in range(R):
        for j in range(C):
            rows=row_ranges[i]; cols=col_ranges[j]
            src=data[i][(j-1)%C]
            bg_src,ac_src,shape=src
            bg_new,ac_new=ac_src,bg_src
            for r in rows:
                for c in cols:
                    out[r][c]=bg_new
            for dr,dc in shape:
                out[rows[dr]][cols[dc]]=ac_new
    return out