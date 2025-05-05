def solve(grid):
    h=len(grid);w=len(grid[0])
    counts={}
    for c in range(1,10):
        cnt=0
        for i in range(h):
            if all(grid[i][j]==c for j in range(w)):cnt+=1
        counts[c]=cnt
    sep=max(counts,key=lambda x:counts[x])
    rows=[i for i in range(h) if all(grid[i][j]==sep for j in range(w))]
    cols=[j for j in range(w) if all(grid[i][j]==sep for i in range(h))]
    rows.sort();cols.sort()
    rd=[rows[i+1]-rows[i] for i in range(len(rows)-1)]
    cd=[cols[i+1]-cols[i] for i in range(len(cols)-1)]
    rh=min(rd)-1;rw=min(cd)-1
    rsegs=[]
    start=0
    if rows and rows[0]>0:
        if rows[0]-1>=rh: rsegs.append((0,rows[0]-1))
    for r in rows:
        s=r+1;e=s+rh-1
        if e<h: rsegs.append((s,e))
    csegs=[]
    if cols and cols[0]>0:
        if cols[0]-1>=rw: csegs.append((0,cols[0]-1))
    for c in cols:
        s=c+1;e=s+rw-1
        if e<w: csegs.append((s,e))
    out=[]
    for rs, re in rsegs:
        row=[]
        for cs, ce in csegs:
            v=0
            for i in range(rs,re):
                for j in range(cs,ce):
                    a=grid[i][j]
                    if a and a!=sep and grid[i][j+1]==a and grid[i+1][j]==a and grid[i+1][j+1]==a:
                        v=a;break
                if v:break
            row.append(v)
        out.append(row)
    return out