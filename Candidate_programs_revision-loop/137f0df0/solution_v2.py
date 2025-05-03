def solve(grid):
    H=len(grid);W=len(grid[0])
    rows=sorted({r for r in range(H) for c in range(W) if grid[r][c]==5})
    cols=sorted({c for r in range(H) for c in range(W) if grid[r][c]==5})
    def intervals(xs):
        if not xs: return []
        res=[];s=xs[0];p=xs[0]
        for x in xs[1:]:
            if x==p+1: p=x
            else:
                res.append((s,p));s=x;p=x
        res.append((s,p))
        return res
    rints=intervals(rows);cints=intervals(cols)
    gapRows=[r for i in range(len(rints)-1) for r in range(rints[i][1]+1,rints[i+1][0])]
    gapCols=[c for i in range(len(cints)-1) for c in range(cints[i][1]+1,cints[i+1][0])]
    r0,r1=rints[0][0],rints[-1][1]
    c0,c1=cints[0][0],cints[-1][1]
    out=[row[:] for row in grid]
    for gr in gapRows:
        for c in range(c0,c1+1):
            if out[gr][c]!=5: out[gr][c]=2
        for c in range(0,c0):
            if out[gr][c]!=5: out[gr][c]=1
        for c in range(c1+1,W):
            if out[gr][c]!=5: out[gr][c]=1
    for gc in gapCols:
        for r in range(r0,r1+1):
            if out[r][gc]!=5: out[r][gc]=2
        for r in range(0,r0):
            if out[r][gc]!=5: out[r][gc]=1
        for r in range(r1+1,H):
            if out[r][gc]!=5: out[r][gc]=1
    return out