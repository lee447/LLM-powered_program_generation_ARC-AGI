def solve(grid):
    H, W = len(grid), len(grid[0])
    is7row = [all(c==7 for c in row) for row in grid]
    is7col = [all(grid[r][c]==7 for r in range(H)) for c in range(W)]
    top = next(i for i,v in enumerate(is7row) if v)
    bot = H-1-next(i for i,v in enumerate(reversed(is7row)) if v)
    left = next(i for i,v in enumerate(is7col) if v)
    right = W-1-next(i for i,v in enumerate(reversed(is7col)) if v)
    fives = [(r,c) for r in range(H) for c in range(W) if grid[r][c]==5]
    r0 = min(r for r,c in fives); r1 = max(r for r,c in fives)
    c0 = min(c for r,c in fives); c1 = max(c for r,c in fives)
    qs = []
    qs.append((0,r0,0,c0))
    qs.append((0,r0,c1+1,W))
    qs.append((r1+1,H,0,c0))
    qs.append((r1+1,H,c1+1,W))
    def period(a):
        n=len(a)
        for p in range(1,n+1):
            ok=True
            for i in range(n-p):
                if a[i]!=a[i+p]:
                    ok=False; break
            if ok: return p
        return n
    best=None
    for (r0_,r1_,c0_,c1_) in qs:
        sub=[row[c0_:c1_] for row in grid[r0_:r1_]]
        cols=set(v for row in sub for v in row if v not in (0,5,7))
        if len(cols)==2:
            ph=period(sub)
            pw=period([tuple(r[:]) for r in zip(*sub)])
            pw = period(list(zip(*sub)))
            pw = period([list(col) for col in zip(*sub)])
            pw = period(list(map(lambda x:tuple(x),zip(*sub))))
            pw=period([tuple(r) for r in zip(*sub)])
            pw = period([tuple(r) for r in zip(*sub)])
            ph=period(sub)
            pw=period(list(zip(*sub)))
            tile=[row[:pw] for row in sub[:ph]]
            best=tile
            break
    return best