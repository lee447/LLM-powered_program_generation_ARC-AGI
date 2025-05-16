def solve(grid):
    H=len(grid)
    stripes=[]
    prev=None
    for r in range(H):
        c=grid[r][0]
        if c==prev:
            stripes[-1][1]+=1
        else:
            stripes.append([c,1])
            prev=c
    total=H
    W=2*total-2
    out=[[0]*W for _ in range(W)]
    offset=0
    for color,th in stripes:
        r_min=offset
        r_max=W-1-offset
        c_min=offset
        c_max=W-1-offset
        for r in range(r_min,r_min+th):
            for c in range(c_min,c_max+1):
                out[r][c]=color
        for r in range(r_max-th+1,r_max+1):
            for c in range(c_min,c_max+1):
                out[r][c]=color
        for r in range(r_min,r_max+1):
            for c in range(c_min,c_min+th):
                out[r][c]=color
            for c in range(c_max-th+1,c_max+1):
                out[r][c]=color
        offset+=th
    return out