def solve(grid):
    h, w = len(grid), len(grid[0])
    ot, ob, ol, or_ = h, -1, w, -1
    anchors = []
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v == 3:
                if r < ot: ot = r
                if r > ob: ob = r
                if c < ol: ol = c
                if c > or_: or_ = c
            elif v == 6:
                anchors.append((r, c))
    nt, nb, nl, nr = ot, ob, ol, or_
    for r, c in anchors:
        if c > or_: nr = max(nr, c-1)
        if c < ol: nl = min(nl, c+1)
        if r < ot: nt = min(nt, r+1)
        if r > ob: nb = max(nb, r-1)
    out = [[0]*w for _ in range(h)]
    for r, c in anchors:
        out[r][c] = 6
    for c in range(nl, nr+1):
        out[nt][c] = 3
        out[nb][c] = 3
    for r in range(nt, nb+1):
        out[r][nl] = 3
        out[r][nr] = 3
    return out