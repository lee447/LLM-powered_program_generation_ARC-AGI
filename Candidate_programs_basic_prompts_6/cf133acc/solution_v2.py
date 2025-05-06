def solve(grid):
    H=len(grid)
    W=len(grid[0])
    out=[row[:] for row in grid]
    for y in range(H):
        row=grid[y]
        for C in set(row):
            if C==0: continue
            segs=[]
            x=0
            while x<W:
                if row[x]==C:
                    s=x
                    while x+1<W and row[x+1]==C:
                        x+=1
                    segs.append((s,x))
                x+=1
            if len(segs)==2 and segs[0][1]+2==segs[1][0]:
                gap=segs[0][1]+1
                for yy in range(y+1):
                    if out[yy][gap]==0:
                        out[yy][gap]=C
    return out