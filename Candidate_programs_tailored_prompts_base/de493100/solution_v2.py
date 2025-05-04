def solve(grid):
    h, w = len(grid), len(grid[0])
    best = None
    for col in range(10):
        coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == col]
        if not coords: continue
        minr = min(r for r, c in coords)
        maxr = max(r for r, c in coords)
        minc = min(c for r, c in coords)
        maxc = max(c for r, c in coords)
        H, W = maxr - minr + 1, maxc - minc + 1
        if H * W != len(coords): continue
        if all(grid[r][c] == col for r in range(minr, maxr + 1) for c in range(minc, maxc + 1)):
            area = H * W
            if best is None or area > best[0]:
                best = (area, col, minr, maxr, minc, maxc)
    if not best:
        return []
    _, acol, r0, r1, c0, c1 = best
    H, W = r1 - r0 + 1, c1 - c0 + 1
    dirs = [(-H, 0), (H, 0), (0, -W), (0, W)]
    for dr, dc in dirs:
        rr0, cc0 = r0 + dr, c0 + dc
        rr1, cc1 = rr0 + H - 1, cc0 + W - 1
        if 0 <= rr0 <= rr1 < h and 0 <= cc0 <= cc1 < w:
            block = [grid[r][cc0:cc1+1] for r in range(rr0, rr1+1)]
            if all(cell != acol for row in block for cell in row):
                return block
    return []