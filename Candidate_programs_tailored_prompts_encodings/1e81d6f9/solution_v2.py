def solve(grid):
    h = max(r for r, row in enumerate(grid) if 5 in row) + 1
    out = [row[:] for row in grid]
    for r in range(h, len(grid)):
        if (r - h) % 4 == 0:
            non_anchor = [c for c, v in enumerate(grid[r]) if v != 0 and v != 5]
            if non_anchor:
                cmax = max(non_anchor)
                out[r][cmax] = 0
    return out