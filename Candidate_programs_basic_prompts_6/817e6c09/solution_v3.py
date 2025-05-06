def solve(grid):
    h = len(grid)
    w = len(grid[0])
    tl = []
    for r in range(h-1):
        for c in range(w-1):
            if grid[r][c]==2 and grid[r][c+1]==2 and grid[r+1][c]==2 and grid[r+1][c+1]==2:
                tl.append((r,c))
    best = (0,0,0)
    for s in range(-w, w+1):
        cnts = {}
        for r,c in tl:
            b = c - s*r
            cnts[b] = cnts.get(b,0) + 1
        for b, cnt in cnts.items():
            if cnt > best[0]:
                best = (cnt, s, b)
    _, s, b = best
    out = [row[:] for row in grid]
    for r in range(h-1):
        c0 = s*r + b
        c0 = int(round(c0))
        if 0 <= c0 < w-1:
            for dr in (0,1):
                for dc in (0,1):
                    out[r+dr][c0+dc] = 8
    return out