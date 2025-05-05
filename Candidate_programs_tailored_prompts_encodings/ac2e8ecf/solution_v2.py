def solve(grid):
    h=len(grid); w=len(grid[0])
    rings=[]
    for i in range(h):
        for j in range(w):
            if grid[i][j]==0: continue
            for s in (3,4):
                if i+s<=h and j+s<=w:
                    v=grid[i][j]
                    ok=True
                    for k in range(s):
                        if grid[i][j+k]!=v or grid[i+s-1][j+k]!=v or grid[i+k][j]!=v or grid[i+k][j+s-1]!=v:
                            ok=False; break
                    if not ok: continue
                    for ii in range(i+1,i+s-1):
                        for jj in range(j+1,j+s-1):
                            if grid[ii][jj]!=0:
                                ok=False; break
                        if not ok: break
                    if ok:
                        rings.append({'x':j,'size':s,'v':v})
    keep=[]
    bycol={}
    for r in rings:
        bycol.setdefault(r['v'], []).append(r)
    for v,rs in bycol.items():
        if len(rs)>1:
            xs=sorted(rs, key=lambda r:r['size'])
            keep+= [r for r in rs if r['size']>xs[0]['size']]
        else:
            keep+=rs
    small=sorted([r for r in keep if r['size']==3], key=lambda r:r['x'])
    large=sorted([r for r in keep if r['size']==4], key=lambda r:r['x'])
    out=[[0]*w for _ in range(h)]
    x=1
    for r in small:
        for k in range(r['size']):
            out[0][x+k]=r['v']
            out[r['size']-1][x+k]=r['v']
            out[0+k][x]=r['v']
            out[0+k][x+r['size']-1]=r['v']
        x+=r['size']+1
    x=1
    y0=h-4
    for r in large:
        for k in range(r['size']):
            out[y0][x+k]=r['v']
            out[y0+r['size']-1][x+k]=r['v']
            out[y0+k][x]=r['v']
            out[y0+k][x+r['size']-1]=r['v']
        x+=r['size']+1
    return out