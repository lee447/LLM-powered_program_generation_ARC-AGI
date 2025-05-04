def solve(grid):
    h=len(grid);w=len(grid[0])
    shape=[(r,c) for r in range(h) for c in range(w) if grid[r][c]!=0]
    drs={r-c for r,c in shape}
    scs={r+c for r,c in shape}
    def is_path():
        if len(shape)<3: return False
        neigh={p:[] for p in shape}
        for r,c in shape:
            for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)):
                q=(r+dr,c+dc)
                if q in neigh:
                    neigh[(r,c)].append(q)
        degs=[len(neigh[p]) for p in shape]
        if any(d>2 for d in degs): return False
        if sum(degs)!=2*(len(shape)-1): return False
        seen={shape[0]}
        stack=[shape[0]]
        while stack:
            p=stack.pop()
            for q in neigh[p]:
                if q not in seen:
                    seen.add(q); stack.append(q)
        return len(seen)==len(shape)
    if len(drs)==1:
        new=2
    elif len(scs)==1:
        new=1
    elif is_path():
        new=4
    else:
        new=2
    out=[[new]*w for _ in range(h)]
    for r,c in shape:
        out[r][c]=0
    return out