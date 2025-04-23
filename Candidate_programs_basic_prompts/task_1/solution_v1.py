def solve(grid):
    R=len(grid); C=len(grid[0])
    segs_by_row={}
    for r in range(R):
        segs=[]
        c=0
        while c<C:
            if grid[r][c]!=0:
                c0=c
                while c<C and grid[r][c]!=0: c+=1
                if c-c0>=3: segs.append((c0,c-1))
            else:
                c+=1
        if segs: segs_by_row[r]=segs
    # collect segment rows
    seg_rows={}
    for r,segs in segs_by_row.items():
        for seg in segs:
            seg_rows.setdefault(seg,[]).append(r)
    # find best left block
    best_score=-1
    for (c0,c1),rows in seg_rows.items():
        w=c1-c0+1
        rs=sorted(rows)
        # compute max consecutive
        cur=1; maxc=1
        for i in range(1,len(rs)):
            if rs[i]==rs[i-1]+1:
                cur+=1
            else:
                maxc=max(maxc,cur); cur=1
        maxc=max(maxc,cur)
        score=w*maxc
        if score>best_score:
            best_score=score; left_seg=(c0,c1); H=maxc
    left0,left1=left_seg; W=left1-left0+1
    # find groups of start rows
    rows=sorted(seg_rows[left_seg])
    groups=[]
    for r in rows:
        if all(r+i in rows for i in range(H)):
            groups.append(r)
    # pick unique starts
    starts=sorted(set(groups))
    # find dx from first group row
    r0=starts[0]
    rights=[c0 for (c0,c1) in segs_by_row[r0] if c1-c0+1>=W and c0!=left0]
    dx=rights[0]-left0 if rights else 0
    # extract pattern
    pattern=[grid[r0+i][left0:left0+W] for i in range(H)]
    # build output
    out=[[0]*C for _ in range(R)]
    for y0 in starts:
        for i in range(H):
            for j in range(W):
                out[y0+i][left0+j]=pattern[i][j]
                if dx:
                    out[y0+i][left0+dx+j]=pattern[i][j]
    return out