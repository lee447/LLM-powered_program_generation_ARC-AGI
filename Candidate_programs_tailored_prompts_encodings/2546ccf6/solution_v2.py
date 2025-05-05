def solve(grid):
    R=len(grid)
    C=len(grid[0])
    rows=[]
    for i in range(R):
        s=set(grid[i])
        if len(s)==1 and next(iter(s))!=0:
            rows.append(i)
    cols=[]
    for j in range(C):
        s={grid[i][j] for i in range(R)}
        if len(s)==1 and next(iter(s))!=0:
            cols.append(j)
    h=sorted(rows)
    v=sorted(cols)
    templates={}
    for i,hr in enumerate(h):
        r0=hr+1
        r1=(h[i+1]-1 if i+1<len(h) else R-1)
        for j,vc in enumerate(v):
            c0=vc+1
            c1=(v[j+1]-1 if j+1<len(v) else C-1)
            offs=[]
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    val=grid[r][c]
                    if val!=0:
                        offs.append((r-hr,c-vc,val))
            if offs:
                key=tuple(sorted(offs))
                if key not in templates:
                    templates[key]={'offs':offs,'rs':set(),'cs':set()}
                templates[key]['rs'].add(i)
                templates[key]['cs'].add(j)
    out=[row[:] for row in grid]
    for t in templates.values():
        offs=t['offs']
        for i in t['rs']:
            for j in t['cs']:
                hr=h[i]
                vc=v[j]
                for dr,dc,val in offs:
                    r=hr+dr
                    c=vc+dc
                    out[r][c]=val
    return out