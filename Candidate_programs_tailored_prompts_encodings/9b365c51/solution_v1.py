def solve(grid):
    H, W = len(grid), len(grid[0])
    bars = [c for c in range(W) if grid[0][c] != 0 and all(grid[r][c] != 0 for r in range(H))]
    palette = [grid[0][c] for c in bars]
    coords = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 8]
    if not coords:
        return [[0]*W for _ in range(H)]
    cols = [c for _, c in coords]
    cmin, cmax = min(cols), max(cols)
    denom = cmax - cmin + 1
    P = len(palette)
    out = [[0]*W for _ in range(H)]
    for r, c in coords:
        a = (c - cmin + 1) * P
        idx = (a + denom - 1)//denom - 1
        if idx < 0: idx = 0
        if idx >= P: idx = P-1
        out[r][c] = palette[idx]
    return out