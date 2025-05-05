def solve(grid):
    h=len(grid); w=len(grid[0])
    out=[]
    for row in grid:
        zeros=[i for i,v in enumerate(row) if v==0]
        first_zero=zeros[0] if zeros else w
        seg=[v for v in row[:first_zero] if v!=0]
        if not seg:
            cycle=[1]
        else:
            for L in range(1,len(seg)+1):
                ok=True
                for i in range(len(seg)):
                    if seg[i]!=seg[i%L]:
                        ok=False
                        break
                if ok:
                    cycle=seg[:L]
                    break
        out.append([cycle[i%len(cycle)] for i in range(w)])
    return out