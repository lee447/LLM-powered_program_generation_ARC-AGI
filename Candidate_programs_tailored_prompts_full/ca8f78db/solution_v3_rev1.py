def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    stripe_rows = [r for r in range(h) if any(cell > bg for cell in grid[r])]
    base = next(r for r in stripe_rows if 0 not in grid[r])
    pattern = grid[base]
    for L in range(1, w + 1):
        if all(pattern[i] == pattern[i % L] for i in range(w)):
            break
    cycle = pattern[:L]
    out = [row[:] for row in grid]
    for r in range(h):
        for c in range(w):
            if grid[r][c] == 0:
                out[r][c] = cycle[c % L] if r in stripe_rows else bg
    return out