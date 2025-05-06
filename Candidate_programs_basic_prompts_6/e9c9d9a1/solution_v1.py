def solve(grid):
    H=len(grid);W=len(grid[0])
    stripe_rows=[r for r in range(H) if all(grid[r][c]==3 for c in range(W))]
    stripe_cols=[c for c in range(W) if all(grid[r][c]==3 for r in range(H))]
    br=[];prev=-1
    for r in stripe_rows:
        if r-prev>1:br.append((prev+1,r-1))
        prev=r
    if H-1>prev:br.append((prev+1,H-1))
    bc=[];prev=-1
    for c in stripe_cols:
        if c-prev>1:bc.append((prev+1,c-1))
        prev=c
    if W-1>prev:bc.append((prev+1,W-1))
    R=len(br);C=len(bc)
    out=[row[:] for row in grid]
    for i,(r0,r1) in enumerate(br):
        for j,(c0,c1) in enumerate(bc):
            for r in range(r0,r1+1):
                for c in range(c0,c1+1):
                    if grid[r][c]!=3:
                        if i==0 and j==0: out[r][c]=2
                        elif i==0 and j==C-1: out[r][c]=4
                        elif i==R-1 and j==0: out[r][c]=1
                        elif i==R-1 and j==C-1: out[r][c]=8
                        elif 0<i<R-1 and 0<j<C-1: out[r][c]=7
    return out