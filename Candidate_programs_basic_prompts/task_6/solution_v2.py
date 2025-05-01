def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    nz_rows = [r for r in range(h) if any(grid[r][c] != 0 for c in range(w))]
    nz_cols = [c for c in range(w) if any(grid[r][c] != 0 for r in range(h))]
    min_r, max_r = min(nz_rows), max(nz_rows)
    min_c, max_c = min(nz_cols), max(nz_cols)
    stripe_rows = [r for r in range(min_r+1, max_r) if all(grid[r][c] == 0 for c in range(w))]
    stripe_cols = [c for c in range(min_c+1, max_c) if all(grid[r][c] == 0 for r in range(h))]
    for r in stripe_rows:
        for c in range(w):
            out[r][c] = 2 if min_c <= c <= max_c else 1
    for c in stripe_cols:
        for r in range(h):
            out[r][c] = 2 if min_r <= r <= max_r else 1
    return out