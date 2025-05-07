def solve(grid):
    h, w = len(grid), len(grid[0])
    coords = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 8]
    if not coords:
        return grid
    r0 = min(r for r, _ in coords)
    c0 = min(c for _, c in coords)
    S = [(r - r0, c - c0) for r, c in coords]
    H0 = max(r for r, _ in S) + 1
    W0 = max(c for _, c in S) + 1
    shapes = []
    s = S; H, W = H0, W0
    for _ in range(4):
        shapes.append((s, H, W))
        s = [(c, H - 1 - r) for r, c in s]
        H, W = W, H
    out = [row[:] for row in grid]
    for s_rel, hh, ww in shapes:
        for i in range(h - hh + 1):
            for j in range(w - ww + 1):
                if all(grid[i + dr][j + dc] == 3 for dr, dc in s_rel):
                    for dr, dc in s_rel:
                        out[i + dr][j + dc] = 8
    return out