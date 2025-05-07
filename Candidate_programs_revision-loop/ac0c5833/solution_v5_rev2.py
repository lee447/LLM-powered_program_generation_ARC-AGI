def solve(grid):
    h, w = len(grid), len(grid[0])
    twos = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 2]
    if not twos:
        return [row[:] for row in grid]
    seen = [[False]*w for _ in range(h)]
    comps = []
    for y, x in twos:
        if not seen[y][x]:
            stack = [(y, x)]
            comp = []
            seen[y][x] = True
            while stack:
                cy, cx = stack.pop()
                comp.append((cy, cx))
                for dy, dx in ((1,0),(-1,0),(0,1),(0,-1)):
                    ny, nx = cy+dy, cx+dx
                    if 0 <= ny < h and 0 <= nx < w and not seen[ny][nx] and grid[ny][nx] == 2:
                        seen[ny][nx] = True
                        stack.append((ny, nx))
            comps.append(comp)
    twos0 = max(comps, key=len)
    fours = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 4]
    def sgn(v):
        return 1 if v>0 else -1 if v<0 else 0
    cands = []
    for fy, fx in fours:
        sdy = {sgn(ty-fy) for ty, tx in twos0 if ty!=fy}
        sdx = {sgn(tx-fx) for ty, tx in twos0 if tx!=fx}
        if len(sdy)==1 and len(sdx)==1:
            cands.append((fy, fx))
    if not cands:
        return [row[:] for row in grid]
    def mindist(f):
        fy, fx = f
        return min(abs(fy-ty)+abs(fx-tx) for ty, tx in twos0)
    py, px = min(cands, key=mindist)
    M = [(ty-py, tx-px) for ty, tx in twos0]
    out = [row[:] for row in grid]
    for fy, fx in cands:
        if (fy, fx) == (py, px):
            continue
        for dy, dx in M:
            y, x = fy+dy, fx+dx
            if 0 <= y < h and 0 <= x < w and out[y][x] == 0:
                out[y][x] = 2
    return out