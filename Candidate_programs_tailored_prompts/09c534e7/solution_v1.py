def solve(grid):
    H, W = len(grid), len(grid[0])
    frames = []
    for y in range(H-3):
        for x in range(W-3):
            if grid[y][x]==1 and grid[y][x+3]==1 and grid[y+3][x]==1 and grid[y+3][x+3]==1:
                ok = True
                for i in range(4):
                    if grid[y+i][x]!=1 or grid[y+i][x+3]!=1 or grid[y][x+i]!=1 or grid[y+3][x+i]!=1:
                        ok = False; break
                if ok:
                    frames.append((y,x))
    ys = sorted({y for y,x in frames})
    xs = sorted({x for y,x in frames})
    def idx(v, arr):
        return arr.index(v)
    pats = {}
    for y,x in frames:
        r,c = idx(y,ys), idx(x,xs)
        p = tuple(grid[y+dy][x+dx] for dy in (1,2) for dx in (1,2))
        pats.setdefault(p, []).append((r,c,y,x))
    tpl = next(p for p, lst in pats.items() if len(lst)==1)
    def rot(p, k):
        a,b,c,d = p
        if k==0: return (a,b,c,d)
        if k==1: return (c,a,d,b)
        if k==2: return (d,c,b,a)
        if k==3: return (b,d,a,c)
    out = [row[:] for row in grid]
    for y,x in frames:
        r,c = idx(y,ys), idx(x,xs)
        k = (r+c) % 4
        p2 = rot(tpl, k)
        it = iter(p2)
        for dy in (1,2):
            for dx in (1,2):
                out[y+dy][x+dx] = next(it)
    return out