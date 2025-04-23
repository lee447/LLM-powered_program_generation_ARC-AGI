def solve(grid):
    segs={}
    for i,row in enumerate(grid):
        for j,v in enumerate(row):
            if v:
                segs.setdefault(v,[]).append((i,j))
    items=[(c,len(cells)) for c,cells in segs.items()]
    items.sort(key=lambda x:-x[1])
    size=items[0][1]
    out=[[0]*size for _ in range(size)]
    for k,(c,l) in enumerate(items):
        if k<len(items)-1:
            for x in range(k,size-k): out[k][x]=c; out[size-1-k][x]=c
            for y in range(k,size-k): out[y][k]=c; out[y][size-1-k]=c
        else:
            for i in range(size):
                for j in range(size):
                    if out[i][j]==0: out[i][j]=c
    return out