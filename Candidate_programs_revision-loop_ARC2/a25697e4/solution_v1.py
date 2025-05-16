def solve(grid):
    H, W = len(grid), len(grid[0])
    regions = {}
    for r in range(H):
        for c in range(W):
            v = grid[r][c]
            if v != 1:
                if v not in regions:
                    regions[v] = [r, r, c, c]
                else:
                    regions[v][0] = min(regions[v][0], r)
                    regions[v][1] = max(regions[v][1], r)
                    regions[v][2] = min(regions[v][2], c)
                    regions[v][3] = max(regions[v][3], c)
    patterns = {}
    for v, (r0, r1, c0, c1) in regions.items():
        patterns[v] = [row[c0:c1+1] for row in grid[r0:r1+1]]
    out = [[1]*W for _ in range(H)]
    base = min(r1 - r0 + 1 for r0, r1, _, _ in regions.values())
    xpos = 0
    for v in sorted(patterns, key=lambda v: (-(regions[v][1]-regions[v][0]+1), v)):
        pat = patterns[v]
        h, w = len(pat), len(pat[0])
        y0 = base - h
        for i in range(h):
            for j in range(w):
                out[y0+i][xpos+j] = pat[i][j]
        xpos += w
    return out