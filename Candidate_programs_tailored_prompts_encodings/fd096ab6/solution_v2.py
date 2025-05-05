def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    clusters = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 1:
                clusters.setdefault(v, []).append((r, c))
    for v, pts in clusters.items():
        rs = [r for r, c in pts]
        cs = [c for r, c in pts]
        r0, r1 = min(rs), max(rs)
        c0, c1 = min(cs), max(cs)
        size = max(r1 - r0 + 1, c1 - c0 + 1)
        for dr in range(size):
            for dc in range(size):
                rr, cc = r0 + dr, c0 + dc
                if 0 <= rr < h and 0 <= cc < w:
                    out[rr][cc] = v
    return out