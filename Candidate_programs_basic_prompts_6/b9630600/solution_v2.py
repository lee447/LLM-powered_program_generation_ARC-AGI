def solve(grid):
    H=len(grid);W=len(grid[0])
    orig=[row[:] for row in grid]
    res=[row[:] for row in grid]
    for y in range(1,H-1):
        segs=[]
        x=0
        while x<W:
            if orig[y][x]==3:
                s=x
                while x+1<W and orig[y][x+1]==3:
                    x+=1
                segs.append((s,x))
            x+=1
        for (s,e),(ns,ne) in zip(segs,segs[1:]):
            if ns>e+1:
                a,e1=s,e
                b=ns
                span=range(e1,b+1)
                if not all(orig[y-1][k]==3 for k in span) and not all(orig[y+1][k]==3 for k in span):
                    for k in span:
                        res[y][k]=3
    return res