def solve(grid):
    H=len(grid);W=len(grid[0])
    barCols=[]
    for c in range(W):
        s={grid[r][c] for r in range(H)}
        if len(s)==1 and next(iter(s))!=0:
            barCols.append(c)
    barCols.sort()
    barColors=[grid[0][c] for c in barCols]
    barSet=set(barCols)
    bands=[]
    for r in range(H):
        nonbar=[grid[r][c] for c in range(W) if c not in barSet]
        if nonbar:
            s=set(nonbar)
            if len(s)==1 and nonbar[0]!=0:
                color=nonbar[0]
                full=all(grid[r][c]==color for c in range(W))
                bands.append((r,color,full))
    bands.sort(key=lambda x:x[0])
    B=len(barCols);N=len(bands)
    out=[]
    for i in range(N+1):
        zr=[0]
        for bc in barColors:
            zr+=[bc,0]
        out.append(zr)
        if i<N:
            _,color,full=bands[i]
            if full:
                out.append([color]*(2*B+1))
            else:
                row=[color]
                for bc in barColors:
                    row+=[bc,color]
                out.append(row)
    return out