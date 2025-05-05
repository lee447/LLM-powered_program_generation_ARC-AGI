def solve(grid):
    h, w = len(grid), len(grid[0])
    base = [(0,0),(1,0),(2,0),(2,1)]
    patterns = set()
    for rot in range(4):
        pts = base
        for _ in range(rot):
            pts = [(c, -r) for r, c in pts]
        for flip in (1, -1):
            pts2 = [(r, c * flip) for r, c in pts]
            mr = min(r for r, c in pts2)
            mc = min(c for r, c in pts2)
            norm = tuple(sorted(((r - mr, c - mc) for r, c in pts2)))
            patterns.add(norm)
    lcount = 0
    for pat in patterns:
        ph = max(r for r, c in pat) + 1
        pw = max(c for r, c in pat) + 1
        for i in range(h - ph + 1):
            for j in range(w - pw + 1):
                ok = True
                for dr, dc in pat:
                    if grid[i + dr][j + dc] != 5:
                        ok = False
                        break
                if ok:
                    lcount += 1
    if lcount:
        return [[0] for _ in range(lcount)]
    vcount = 0
    for c in range(w):
        r = 0
        while r < h - 1:
            if grid[r][c] == 5 and grid[r+1][c] == 5:
                if r == 0 or grid[r-1][c] != 5:
                    vcount += 1
                rr = r + 1
                while rr < h and grid[rr][c] == 5:
                    rr += 1
                r = rr
            else:
                r += 1
    return [[0] for _ in range(vcount)]