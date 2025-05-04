def solve(grid):
    H, W = len(grid), len(grid[0])
    pts = [(r, c) for r in range(H) for c in range(W) if grid[r][c] != 0]
    minr = min(r for r, _ in pts)
    maxr = max(r for r, _ in pts)
    minc = min(c for _, c in pts)
    maxc = max(c for _, c in pts)
    h = maxr - minr + 1
    w = maxc - minc + 1
    orig = grid[minr][minc]
    comp = 3 if orig == 6 else 6
    shape = [(r, c) for r in range(minr, minr + h) for c in range(minc, minc + w) if grid[r][c] == orig]
    def fH(p): return (H - 1 - p[0], p[1])
    def fV(p): return (p[0], W - 1 - p[1])
    def fR(p): return (p[1], H - 1 - p[0])
    trans = [
        (lambda p: p, orig),
        (fH, orig),
        (fV, orig),
        (lambda p: fH(fV(p)), orig),
        (fR, comp),
        (lambda p: fH(fR(p)), comp),
        (lambda p: fV(fR(p)), comp),
        (lambda p: fH(fV(fR(p))), comp)
    ]
    out = [[0]*W for _ in range(H)]
    for fn, col in trans:
        for r, c in shape:
            rr, cc = fn((r, c))
            out[rr][cc] = col
    return out