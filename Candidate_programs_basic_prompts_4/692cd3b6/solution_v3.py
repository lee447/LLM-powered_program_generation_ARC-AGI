def solve(grid):
    h, w = len(grid), len(grid[0])
    centers = [(r, c) for r in range(h) for c in range(w) if grid[r][c] == 5]
    (r1, c1), (r2, c2) = sorted(centers)
    top, bot = min(r1, r2), max(r1, r2)
    left, right = min(c1, c2), max(c1, c2)
    if c1 < c2:
        c0, c3 = left, right - 2
    else:
        c0, c3 = left + 2, right
    if r1 < r2:
        r0, r3 = top + 2, bot - 2
    else:
        r0, r3 = top, bot
    out = [row[:] for row in grid]
    for r in range(r0, r3 + 1):
        for c in range(c0, c3 + 1):
            if out[r][c] == 0:
                out[r][c] = 4
    return out