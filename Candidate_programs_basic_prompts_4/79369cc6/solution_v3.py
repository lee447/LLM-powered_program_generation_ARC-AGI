def solve(grid):
    H, W = len(grid), len(grid[0])
    fours = [(r, c) for r in range(H) for c in range(W) if grid[r][c] == 4]
    if not fours:
        return grid
    min_r = min(r for r, _ in fours)
    max_r = max(r for r, _ in fours)
    min_c = min(c for _, c in fours)
    max_c = max(c for _, c in fours)
    h = max_r - min_r + 1
    w = max_c - min_c + 1
    orig = [(r - min_r, c - min_c) for r, c in fours]
    rot90 = [(c, h - 1 - r) for r, c in orig]
    rot270 = [(w - 1 - c, r) for r, c in orig]
    out = [row[:] for row in grid]
    for shape in (rot90, rot270):
        best = None
        for dr in range(H):
            for dc in range(W):
                ok = True
                for rr, cc in shape:
                    r0, c0 = dr + rr, dc + cc
                    if r0 < 0 or r0 >= H or c0 < 0 or c0 >= W or grid[r0][c0] == 4:
                        ok = False
                        break
                if not ok:
                    continue
                if best is None:
                    best = (dr, dc)
        if best:
            dr, dc = best
            for rr, cc in shape:
                out[dr + rr][dc + cc] = 4
    return out