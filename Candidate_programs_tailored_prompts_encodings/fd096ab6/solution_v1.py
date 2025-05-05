def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = max({c: sum(row.count(c) for row in grid) for row in grid for c in set(row)} , key=lambda x: sum(row.count(x) for row in grid))
    cells = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != bg:
                cells.setdefault(v, []).append((r, c))
    out = [row[:] for row in grid]
    for v, pts in cells.items():
        rs = [r for r, _ in pts]
        cs = [c for _, c in pts]
        r0, c0 = min(rs), min(cs)
        side = max(max(rs) - r0 + 1, max(cs) - c0 + 1)
        for r in range(r0, r0 + side):
            for c in range(c0, c0 + side):
                out[r][c] = v
    return out