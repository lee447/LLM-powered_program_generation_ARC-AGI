from collections import Counter, deque
def solve(grid):
    H, W = len(grid), len(grid[0])
    frames = []
    for y in range(H-3):
        for x in range(W-3):
            ok = True
            for i in range(4):
                if grid[y+i][x]!=1 or grid[y+i][x+3]!=1 or grid[y][x+i]!=1 or grid[y+3][x+i]!=1:
                    ok = False; break
            if ok:
                frames.append((y, x))
    if not frames:
        return grid
    ys = sorted({y for y, x in frames})
    xs = sorted({x for y, x in frames})
    y2r = {y:i for i, y in enumerate(ys)}
    x2c = {x:i for i, x in enumerate(xs)}
    rc2yx = {}
    for y, x in frames:
        rc2yx[(y2r[y], x2c[x])] = (y, x)
    p_map = {}
    for rc, (y, x) in rc2yx.items():
        a = grid[y+1][x+1]; b = grid[y+1][x+2]
        c = grid[y+2][x+1]; d = grid[y+2][x+2]
        p_map[rc] = (a, b, c, d)
    cnt = Counter(p_map.values())
    pdefault = max(cnt, key=cnt.get)
    seeds = [(rc, p) for rc, p in p_map.items() if p!=pdefault]
    assigned = {}
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for rc0, p0 in seeds:
        if rc0 in assigned: continue
        q = deque([rc0])
        assigned[rc0] = (rc0, p0)
        while q:
            r, c = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if (nr, nc) in rc2yx and (nr, nc) not in assigned:
                    assigned[(nr, nc)] = (rc0, p0)
                    q.append((nr, nc))
    out = [row[:] for row in grid]
    def rot(p, k):
        a, b, c, d = p
        if k==0: return (a, b, c, d)
        if k==1: return (c, a, d, b)
        if k==2: return (d, c, b, a)
        return (b, d, a, c)
    for (r, c), (seed_rc, p0) in assigned.items():
        r0, c0 = seed_rc
        y, x = rc2yx[(r, c)]
        k = ((r+c) - (r0+c0)) % 4
        p2 = rot(p0, k)
        out[y+1][x+1] = p2[0]
        out[y+1][x+2] = p2[1]
        out[y+2][x+1] = p2[2]
        out[y+2][x+2] = p2[3]
    return out